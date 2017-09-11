<?php 
	    //Realizando a conexão com o banco
	    require 'config.php'; 
	    require 'conexao.php';
	    $link = DB_connect();

	    //Recebe 
	    $nome= $_POST['username'];
	    $email= $_POST['email'];

		//Consulta SQL de inserção:
		$query = "INSERT INTO user (Nome, Email) VALUES ('$nome', '$email')"; 
		$result = @mysqli_query($link, $query) or die(mysqli_connect_error($link));

		if($result){
			echo "Cadastrado com sucesso";
			include 'form2.php';
		}else{
			echo "Deu ruim";
		}
	    //Fecha Conexão	
	    DB_Close($link);
?>
