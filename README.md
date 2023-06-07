# Marvel Superheroes Data Quality Checks

This repository contains code and configuration files to perform data quality checks on Marvel superheroes data using the Great Expectations library.



`Great Expectations` is the leading tool for **validating**, **documenting**, and **profiling** your data to maintain quality and improve communication between teams.

With `Great Expectations`, you can assert what you expect from the data you load and transform, and catch data issues quickly – *Expectations* are basically unit tests for your data. Not only that, but `Great Expectations` also creates data documentation and data quality reports from those *Expectations*. Data science and data engineering teams use `Great Expectations` to:
- Test data they ingest from other teams or vendors and ensure its validity. 
- Validate data they transform as a step in their data pipeline in order to ensure the correctness of transformations. 
- Prevent data quality issues from slipping into data products. 
- Streamline knowledge capture from subject-matter experts and make implicit knowledge explicit. 
- Develop rich, shared documentation of their data.

### Expectations
*Expectations* are assertions about your data. In `Great Expectations`, those assertions are expressed in a declarative language in the form of simple, human-readable Python methods. 

### Automated data profiling
Writing pipeline tests from scratch can be tedious and overwhelming. `Great Expectations` jump starts the process by providing automated data profiling. The library profiles your data to get basic statistics, and automatically generates a suite of Expectations based on what is observed in the data.

### Data Validation
Once you’ve created your *Expectations*, `Great Expectations` can load any batch or several batches of data to validate with your suite of *Expectations*. `Great Expectations` tells you whether each *Expectation* in an *Expectation Suite* passes or fails, and returns any unexpected values that failed a test, which can significantly speed up debugging data issues!

### Data docs
`Great Expectations` renders *Expectations* to clean, human-readable documentation, which we call Data Docs, see the screenshot below. These HTML docs contain both your *Expectation Suites* as well as your data Validation Results each time validation is run – think of it as a continuously updated data quality report.
