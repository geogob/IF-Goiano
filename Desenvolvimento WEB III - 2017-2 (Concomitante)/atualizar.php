<?php 
//Recebe 
$id= $_GET['id'];
//echo $id;
require 'config.php'; 
require 'conexao.php';
$link = DB_connect();

//Consulta SQL de select:
$query = "SELECT * FROM user"; 
$result = @mysqli_query($link, $query);
while ($registro = mysqli_fetch_assoc($result)){
    if ($registro["id"]==$id) {
        $nome = $registro["nome"];
        $login = $registro["login"];
    }
}
echo '<form action="atualizar-form.php?id='.$id.'" method="post">';
?>

Nome:  
<input size= "30" type="text" value=<?php echo "$nome"; ?> name="username"/></br>
E-mail: 
<input size= "30" type="text" name="email"/></br>
<input type="submit" value="Atualizar" /></br>           

</form>

	
