<?php 
include "form2.php";

//Realizando a conexão com o banco
	    require 'config.php'; 
	    require 'conexao.php';
	    $link = DB_connect();

	    //Recebe 
	    $id= $_GET['id'];
	     
	     //Recebe 
	    $nome= $_POST['username'];
	    $email= $_POST['email'];
	    
	    echo $id;
		echo $nome;
		echo $email;

		$query ="UPDATE user SET Nome = '$nome', Email = '$email' WHERE id_user = $id";
 		$result = @mysqli_query($link, $query);

	    DB_Close($link);
?>