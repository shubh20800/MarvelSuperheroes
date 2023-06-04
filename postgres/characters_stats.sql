-- Table: public.characters_stats

-- DROP TABLE IF EXISTS public.characters_stats;

CREATE TABLE IF NOT EXISTS public.characters_stats
(
    "Name" character varying COLLATE pg_catalog."default",
    "Alignment" character varying COLLATE pg_catalog."default",
    "Intelligence" integer,
    "Strength" integer,
    "Speed" integer,
    "Durability" integer,
    "Power" integer,
    "Combat" integer,
    "Total" integer
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.characters_stats
    OWNER to postgres;