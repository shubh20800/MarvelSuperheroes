-- Table: public.comics

-- DROP TABLE IF EXISTS public.comics;

CREATE TABLE IF NOT EXISTS public.comics
(
    "comicID" bigint NOT NULL,
    title character varying COLLATE pg_catalog."default",
    "issueNumber" numeric,
    description character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.comics
    OWNER to postgres;