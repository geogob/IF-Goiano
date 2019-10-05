<?php
	$login = $_POST["login"];
	$senha = $_POST["senha"];

	//Realizando a conexão com o banco
	require 'config.php'; 
	require 'conexao.php';
	$link = DB_connect();

	//Consulta SQL de inserção:
	$query = "SELECT * FROM user"; 
	$result = @mysqli_query($link, $query);
	
	$achei=0;
	while ($registro = mysqli_fetch_assoc($result)){
		$emailDB = $registro["email"];
		$senhalDB = $registro["senha"];		
		if ($emailDB==$email && $senhalDB==$senha) {
			$achei=1;
			$nome = $registro["nome"];
		}
	}
	
	if ($achei==0) {
		echo "Acesso negado ou senha e login incorretos";
	}else{
		echo "Bem vindo $nome";
	}	
	//Fecha Conexão	
	DB_Close($link);
?>