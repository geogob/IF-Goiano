<?php

function DB_Close($link){
	mysqli_close($link) or die(mysqli_error($link));
}

//Abrir conexão
function DB_connect(){
	$link = @mysqli_connect(DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE) or die(mysqli_connect_error());

	mysqli_set_charset($link, DB_CHARSET) or die(mysqli_connect_error($link));

	return $link;
}

?>