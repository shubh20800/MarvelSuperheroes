-- Table: public.charactersToComics

-- DROP TABLE IF EXISTS public."charactersToComics";

CREATE TABLE IF NOT EXISTS public."charactersToComics"
(
    "comicID" bigint NOT NULL,
    "characterID" bigint NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."charactersToComics"
    OWNER to postgres;