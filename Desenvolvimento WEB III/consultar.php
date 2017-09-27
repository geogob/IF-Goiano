<?php 
	    //Realizando a conexão com o banco
	    require 'config.php'; 
	    require 'conexao.php';
	    $link = DB_connect();

		//Consulta SQL de inserção:
		$query = "SELECT * FROM user"; 
		$result = @mysqli_query($link, $query);

		echo '<table>';
		echo '<tr>';
		echo '<td> <h2> Nome </h2> </td>';
		echo '<td> <h2> E-mail </h2></td>';
		echo '<td> <h2> Opções </h2> </td>';
		echo '<td>  </td>';
		echo '</tr>';

		while ($registro = mysqli_fetch_assoc($result)) {
			echo '<tr>';
			echo '<td> <i>'.$registro["Nome"].'</i></td>';
			echo '<td> <b>'.$registro["Email"].'</b> </td>';
			$id = $registro["id_user"];
			echo '<td> <a href="deletar.php?id='.$id.'">Deletar</a> </td>';
			echo '<td> <a href="atualizar.php?id='.$id.'">Atualizar</a> </td>';
			echo '</tr>';
		}
		echo '</table>';
	    //Fecha Conexão	
	    DB_Close($link);
?>