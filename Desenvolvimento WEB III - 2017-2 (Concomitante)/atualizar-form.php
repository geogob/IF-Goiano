<?php 
//include "form2.php";

//Realizando a conexão com o banco
require 'config.php'; 
require 'conexao.php';
$link = DB_connect();

//Recebe o id do usuário
$id= $_GET['id'];

//Recebe os dados do usuário
$nome = $_POST['username'];
$email = $_POST['email'];

$query ="UPDATE user SET Nome = '$nome', Email = '$email' WHERE id_user = $id";
$result = @mysqli_query($link, $query);

if ($result) {
	echo "Atualizado com sucesso!!!";
}else{
	echo "Deu ruim!!!";
}

DB_Close($link);
?>