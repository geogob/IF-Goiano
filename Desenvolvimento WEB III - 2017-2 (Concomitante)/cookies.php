<?php
// Cria o mesmo cookie acima só que irá durar três dias
setcookie('usuario', 'Fulano');

// Cria o novo cookie para durar duas horas
setcookie('nome', 'Ciclano', (time() + (6)));

//Apaga sessões
//setcookie('usuario');
//setcookie('x');

//Todos os cookies setados no navegador
print_r($_COOKIE);
?>