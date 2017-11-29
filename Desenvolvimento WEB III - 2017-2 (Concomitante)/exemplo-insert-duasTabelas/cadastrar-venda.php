<?php 
	    //Realizando a conexão com o banco
	    require 'config.php'; 
	    require 'conexao.php';
	    $link = DB_connect();

	    //Recebe todas as variáveis 
	    $produto= $_POST['produto'];
	    $preco= $_POST['preco'];
	    $qnt= $_POST['qnt'];
	    $data= $_POST['data'];

		//Inserção na tabela venda:
		$query_venda = "INSERT INTO venda (Data) VALUES ('$data')"; 
		$result_venda = @mysqli_query($link, $query_venda) or die(mysqli_connect_error($link));

		$id_venda = mysqli_insert_id($link);
		//echo $id_venda;

		//Inserção na tabela produto:
		$query_produto = "INSERT INTO produto (Nome, Preço) VALUES ('$produto', '$preco')"; 
		$result_produto = @mysqli_query($link, $query_produto) or die(mysqli_connect_error($link));

		$id_produto = mysqli_insert_id($link);
		//echo $id_produto;

		//Inserção na tabela Venda_has_Produto:
		$query_vend_prod = "INSERT INTO venda_has_produto (Venda_idVenda,Produto_idProduto, Quantidade) VALUES ('$id_venda', '$id_produto', $qnt)"; 
		$result_vend_prod = @mysqli_query($link, $query_vend_prod) or die(mysqli_connect_error($link));

		//$id_vend_prod = mysqli_insert_id($link);
		//echo $id_vend_prod;


		if($result_produto && $result_venda && $result_vend_prod){
			echo "Cadastrado com sucesso";
			include 'form-venda.php';
		}else{
			echo "Deu ruim";
		}
		
	    //Fecha Conexão	
	    DB_Close($link);
?>
