# Formulário de Cadastro com PHP e MySQL
Este é um exemplo simples de um formulário de cadastro web que coleta informações do usuário e as armazena em um banco de dados MySQL. O projeto utiliza HTML, CSS com um tema escuro e PHP para processamento de dados e interação com o banco de dados.

## Configuração do Banco de Dados
Antes de utilizar o formulário, você precisa configurar o banco de dados e a tabela correspondente. Você pode fazer isso executando os seguintes comandos SQL:
```sql
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
```

Certifique-se de substituir `"seu_usuario"` e `"sua_senha"` pelas credenciais corretas do seu banco de dados MySQL.

## Conteúdo do Projeto
- **FORMULARIO.html**: Este arquivo contém o código HTML para o formulário de cadastro. Ele coleta o nome (EXTRA), email e senha do usuário.

- **FORMULARIO.css**: O arquivo CSS define a aparência do formulário, incluindo o tema escuro. Ele estiliza os elementos HTML para fornecer uma interface atraente.

- **FORMULARIO.php**: O arquivo PHP processa os dados do formulário e realiza a inserção no banco de dados. Ele também realiza a validação dos dados e exibe mensagens de sucesso ou erro.

## Instruções de Uso
1. Configure um servidor web local com suporte a PHP e MySQL.

2. Crie o banco de dados e a tabela conforme os comandos SQL fornecidos anteriormente.

3. Abra o arquivo `FORMULARIO.html` em um navegador da web.

4. Preencha o formulário com as informações desejadas.

5. Clique no botão "Cadastrar" para enviar os dados.

6. Você receberá uma mensagem informando se o cadastro foi realizado com sucesso ou se ocorreu algum erro.

Certifique-se de configurar corretamente o ambiente PHP em seu servidor local para que o projeto funcione adequadamente.