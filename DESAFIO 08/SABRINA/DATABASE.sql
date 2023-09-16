-- Crie um banco de dados chamado "cadastro"
CREATE DATABASE cadastro;

-- Use o banco de dados "cadastro"
USE cadastro;

-- Crie uma tabela chamada "usuarios"
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);
