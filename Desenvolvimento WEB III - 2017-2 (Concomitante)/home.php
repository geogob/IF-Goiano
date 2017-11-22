<?php
//INICIO A SESSÃO
session_start();
 
//Verifico se o usuário está logado no sistema
if ($_SESSION["logado"] != TRUE) {
    header("Location: login.php");
}else {
    echo "<h1>Seja bem-vindo, ".$_SESSION["user"]."</h1>";
}
?>