<?php
//INICIO A SESSÃO
session_start();
 

$login = array("user01", "user02", "user03", "user04", "user05");
$senha = array("senha01", "senha02", "senha03", "senha04", "senha05");
 
//Calculo o tamanho do array $login
$tamArray = count($login);
//Crio uma variável auxiliar
$msg = FALSE;
//Uso um loop para percorrer o array
for ($i = 0; $i < $tamArray; $i++) {
	if ($_POST["login"] == $login[$i] && $_POST["senha"] == $senha[$i]) {
		$msg = TRUE;
		break;
	}
}
//Verifico se a variável auxiliar $msg saiu do loop com o valor TRUE (indicando login efetuado com sucesso)
if ($msg) {
	//Armazeno duas informações na sessão do usuário: se ele está logado, e o login de acesso. A partir desse momento, qualquer página habilitada a trabalhar com variáveis de sessão, poderá resgatar essas variáveis, manipulá-las, sobreescrevê-las etc.
	$_SESSION["logado"] = TRUE;
	$_SESSION["user"] = $_POST["login"];
	//Uso a função header() para fazer o redirecionamento para a página principal do site, uma vez que o login foi executado com sucesso
	header ("Location: home.php");
}else {
	//Caso o login dê errado, devolvo o usuário para a página de login
	header ("Location: login.php");
}
?>

