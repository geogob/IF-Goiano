<?php

//INICIO A SESSÃO COM UM TEMPO DE EXPIRAÇÃO DE 1 MINUTO
//session_cache_expire(1);

//INICIA A SESSÃO
session_start();
$_SESSION["x"] = 1;
$_SESSION["nome"] = "George";
echo $_SESSION["nome"], "<br>"; 
 
$id = session_id();
echo $id, "<br>";

//DESTROI A SESSÃO
if (session_destroy()) {
    echo "Sessão destruída <br>";
}else {
    echo "Não foi possível destruir a sessão <br>";
}

echo $_SESSION["x"];

?>
