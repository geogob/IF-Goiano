<?php 
//Recebe 
	    $id= $_GET['id'];
	    //echo $id;

	    include "form2.php";


echo '<form action="atualizar-form.php?id='.$id.'" method="post">';
?>
            <p>
                Novo nome:  <input size= "30" type="text" name="username" />
            </p>
            <p>
                Novo e-mail: <input size= "30" type="text" name="email" />
            </p>
            <p>
                <input type="submit" value="Enviar" />
            </p>
        </form>

	
