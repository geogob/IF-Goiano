<?php
include 'form2.php';
switch ($_GET['valor']) {
	case 1:
		echo "Cadastrar:";
		include 'form.php';
		break;
	case 2:
		echo "Consultar";
		include 'consultar.php';
		break;
	case 3:
		echo "Excluir";
		include 'deletar.php';
		break;
	case 4:
		echo "Atualizar";
		include 'atualizar.php';
		break;
	default:
		echo "opção errada";
		break;
}

?>
