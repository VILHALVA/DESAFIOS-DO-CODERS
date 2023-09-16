<?php
$host = "localhost";
$usuario = "seu_usuario";
$senha = "sua_senha";
$banco = "cadastro";

$conexao = new mysqli($host, $usuario, $senha, $banco);

if ($conexao->connect_error) {
    die("Erro na conexão com o banco de dados: " . $conexao->connect_error);
}

$nome = $_POST["nome"];
$email = $_POST["email"];
$senha = password_hash($_POST["senha"], PASSWORD_DEFAULT);

$sql = "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)";
$stmt = $conexao->prepare($sql);
$stmt->bind_param("sss", $nome, $email, $senha);

if ($stmt->execute()) {
    echo "Usuário cadastrado com sucesso!";
} 
else {
    echo "Erro ao cadastrar usuário: " . $stmt->error;
}

$stmt->close();
$conexao->close();
?>
