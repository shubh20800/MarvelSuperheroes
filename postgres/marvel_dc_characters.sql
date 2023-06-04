-- Table: public.marvel_dc_characters

-- DROP TABLE IF EXISTS public.marvel_dc_characters;

CREATE TABLE IF NOT EXISTS public.marvel_dc_characters
(
    "ID" bigint NOT NULL,
    "Name" character varying COLLATE pg_catalog."default",
    "Identity" character varying COLLATE pg_catalog."default",
    "Alignment" character varying COLLATE pg_catalog."default",
    "EyeColor" character varying COLLATE pg_catalog."default",
    "HairColor" character varying COLLATE pg_catalog."default",
    "Gender" character varying COLLATE pg_catalog."default",
    "Status" character varying COLLATE pg_catalog."default",
    "Appearances" character varying COLLATE pg_catalog."default",
    "FirstAppearance" character varying COLLATE pg_catalog."default",
    "Year" bigint,
    "Universe" character varying COLLATE pg_catalog."default",
    CONSTRAINT marvel_dc_characters_pkey PRIMARY KEY ("ID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.marvel_dc_characters
    OWNER to postgres;