<?php
include 'form2.php';
switch ($_GET['valor']) {
	case 1:
		echo "Cadastrar:";
		include 'form.php';
		break;
	case 2:
		echo "Consultar";
		break;
	case 3:
		echo "Excluir";
		break;
	case 4:
		echo "Atualizar";
		break;
	default:
		echo "opção errada";
		break;
}

?>
