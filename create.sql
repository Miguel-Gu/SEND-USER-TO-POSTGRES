CREATE SCHEMA IF NOT EXISTS usuario;


CREATE TABLE IF NOT EXISTS usuario.usuario
(
    id                 SERIAL PRIMARY KEY NOT NULL,
    nome               VARCHAR,
    email              VARCHAR,
    cpf                VARCHAR(14),
    datanascimento     DATE,
    cep                VARCHAR(9),
    endereco           VARCHAR,
    numero             VARCHAR,
    complemento        VARCHAR
);