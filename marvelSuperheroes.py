# pip install 'great_expectations[postgresql]'
# pip install great_expectations
from ruamel import yaml
import great_expectations as gx
from great_expectations.data_context import FileDataContext
from great_expectations.core.batch import BatchRequest

datasource_name="my_postgres"
data_connector_name="postgres_data_connector"
schema_name="public"


# ######################      Create a DataContext       ######################
def create_data_context():
    data_context = gx.get_context()

    datasource_config: dict = {
        "name": "my_postgres",
        "class_name": "Datasource",
        "module_name": "great_expectations.datasource",
        "execution_engine": {
            "class_name": "SqlAlchemyExecutionEngine",
            "module_name": "great_expectations.execution_engine",
            "connection_string": "postgresql+psycopg2://postgres:Shellsharma%4092@localhost:5432/postgres"
        },
        "data_connectors": {
            "postgres_data_connector": {
                "class_name": "InferredAssetSqlDataConnector",
                "include_schema_name": True,

            },
        }
    }

    data_context.add_or_update_datasource(**datasource_config)
    # print(data_context)
    return data_context


# ######################    Create batch request with the postgres data     ######################
def create_batch_request(datasource_name, data_connector_name, data_asset_name):
    batch_request = BatchRequest(
        datasource_name=datasource_name,
        data_connector_name=data_connector_name,
        data_asset_name=data_asset_name  # Schema.Tablename
    )
    return batch_request


# ######################     Create an Expectation suite containing all the DQ checks    ######################
def create_expectations_suite(datacontext, expectation_suite_name):
    expectation_suite = datacontext.add_or_update_expectation_suite(expectation_suite_name=expectation_suite_name)
    return expectation_suite



# ######################    Create a Validator    ######################
def create_validator_with_dq_checks(datacontext, batchrequest):
    validator = datacontext.get_validator(
        batch_request= batchrequest,
        expectation_suite_name=expectation_suite_name
    )

    dataset_columns= validator.columns()
    df_val=validator.head(1)

    # ######################  Add Expectations  ######################
    ##################################################################
    # Data Distribution
    for i in range(0,len(dataset_columns)):
            val=df_val.iloc[0, i]
            if(isinstance(val, str)!=True):
                validator.expect_column_mean_to_be_between(dataset_columns[i], auto=True)
                validator.expect_column_stdev_to_be_between(dataset_columns[i], auto=True)
                validator.expect_column_median_to_be_between(dataset_columns[i], auto=True)
                validator.expect_column_max_to_be_between(dataset_columns[i], auto=True)
                validator.expect_column_min_to_be_between(dataset_columns[i], min_value=0)

    # DuplicateCheck
    for i in range(0,len(dataset_columns)):
            val=df_val.iloc[0, i]
            if(isinstance(val, str)):
                validator.expect_column_values_to_be_unique(dataset_columns[i])

    # NullCheck
    for column_name in dataset_columns:
        validator.expect_column_values_to_not_be_null(column_name)

    # Data Validation
    if(data_asset_name=="public.characters_stats"or data_asset_name=="public.marvel_characters_info") :
        validator.expect_column_values_to_be_in_set("Alignment", ["good", "bad", "neutral"])

    if (data_asset_name == "public.marvel_characters_info"):
        validator.expect_column_values_to_be_in_set("Gender", ["Male", "Female","-"])

    if (data_asset_name == "public.marvel_dc_characters"):
        validator.expect_column_values_to_be_in_set("Alignment", ["Good", "Bad", "Neutral", "Reformed Criminals"])
        validator.expect_column_values_to_be_in_set("Status", ["Living", "Deceased"])
        validator.expect_column_values_to_be_in_set("Universe", ["DC", "Marvel"])

    #Schema Check
    validator.expect_table_columns_to_match_ordered_list(dataset_columns)

    validator.save_expectation_suite(discard_failed_expectations=False)


# ######################   Create a checkpoint against which data can be validated   ######################
def create_run_checkpoint_and_get_results(datasource_name, data_connector_name, data_asset_name):
    datacontext= create_data_context()
    batchrequest= create_batch_request(datasource_name, data_connector_name, data_asset_name)
    create_expectations_suite(datacontext, expectation_suite_name)
    create_validator_with_dq_checks(datacontext, batchrequest)

    checkpoint = gx.checkpoint.SimpleCheckpoint(
        name=checkpoint_name,
        data_context=datacontext,
        expectation_suite_name=expectation_suite_name,
        batch_request=batchrequest
    )


    # ######################     Add and save the checkpoint to the data context   ######################
    datacontext.add_or_update_checkpoint(checkpoint=checkpoint)
    checkpoint_result = checkpoint.run()

    validation_result_identifier = checkpoint_result.list_validation_result_identifiers()[0]

    # ######################     Open Results HTML   ######################
    datacontext.open_data_docs(resource_identifier=validation_result_identifier)


if __name__ == "__main__":
    datasets_list = ["marvel_characters_info"]
                    # ["characters_stats"
                     # ,"charactersToComics", "characters", "marvel_characters_info", "marvel_dc_characters", "superheroes_power_matrix"]

    for dataset in datasets_list:
        data_asset_name=schema_name+"."+dataset
        expectation_suite_name = dataset + '_postgres_test_suite'
        checkpoint_name = dataset + '_checkpoint_1'
        create_run_checkpoint_and_get_results(datasource_name, data_connector_name, data_asset_name)