<html lang="pt-br">
    <head>
        <title> DW3 </title>
        <meta charset="utf-8">
        
    </head>
    <body>
        <form action="cadastrar.php" method="post">
            <p>
                Nome: <input size= "30" type="text" name="username"/>
            </p>
            <p>
                E-mail: <input size= "30" type="text" name="email"/>
            </p>
            <p>
                <input type="submit" value="Enviar"/>
            </p>
        </form>
    </body>
</html>
<?php
    echo "<br>";
    include 'consultar.php';
?>