-- Table: public.characters

-- DROP TABLE IF EXISTS public.characters;

CREATE TABLE IF NOT EXISTS public.characters
(
    "characterID" bigint NOT NULL,
    name character varying COLLATE pg_catalog."default",
    CONSTRAINT characters_pkey PRIMARY KEY ("characterID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.characters
    OWNER to postgres;