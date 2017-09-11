<?php 
	    //Realizando a conexão com o banco
	    require 'config.php'; 
	    require 'conexao.php';
	    $link = DB_connect();

	    //Recebe 
	    $id= $_GET['id'];

		//Consulta SQL de inserção:
		$query = "DELETE FROM user WHERE id_user = '$id'"; 
		$result = @mysqli_query($link, $query) or die(mysqli_connect_error($link));

		if($result){
			echo "Removido com sucesso";
			include 'form2.php';
		}else{
			echo "Deu ruim";
		}
	    //Fecha Conexão	
	    DB_Close($link);
?>
