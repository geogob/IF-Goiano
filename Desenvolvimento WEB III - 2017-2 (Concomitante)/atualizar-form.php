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
	    /*Consulta SQL de inserção:
		$query = "SELECT * FROM user WHERE id_user = $id"; 
		$result = @mysqli_query($link, $query);

		while ($registro = mysqli_fetch_assoc($result)) {
			$nome = $registro["Nome"];
			$email = $registro["Email"];
			$id = $registro["id_user"];
		}*/

		$query ="UPDATE user SET Nome = '$nome', Email = '$email' WHERE id_user = $id";
 		$result = @mysqli_query($link, $query);

	    DB_Close($link);
?>