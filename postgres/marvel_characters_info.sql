-- Table: public.marvel_characters_info

-- DROP TABLE IF EXISTS public.marvel_characters_info;

CREATE TABLE IF NOT EXISTS public.marvel_characters_info
(
    "ID" bigint NOT NULL,
    "Name" character varying COLLATE pg_catalog."default",
    "Alignment" character varying COLLATE pg_catalog."default",
    "Gender" character varying COLLATE pg_catalog."default",
    "EyeColor" character varying COLLATE pg_catalog."default",
    "Race" character varying COLLATE pg_catalog."default",
    "HairColor" character varying COLLATE pg_catalog."default",
    "Publisher" character varying COLLATE pg_catalog."default",
    "SkinColor" character varying COLLATE pg_catalog."default",
    "Height" numeric,
    "Weight" numeric,
    CONSTRAINT marvel_characters_info_pkey PRIMARY KEY ("ID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.marvel_characters_info
    OWNER to postgres;