<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum_scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div id="form">
        <form action="save.php" method="post">
            <label for="email">Email</label>
            <input type="email" name="email" required>

            <label for="category">Category</label>
            <select name="category" required>
            	<?php
		$list = ['cars', 'food', 'drink', 'other'];
		for ($i = 0; $i < count($list); $i++)
		{?>
		    <option value=<?php echo $list[$i];?>><?php echo $list[$i];?></option>
		<?php }?>  
            </select>
        
            <label for="title">Title</label>
            <input type="text" name="title" required>

            <label for="description">Description</label>
            <textarea rows="3" name="description"></textarea>
        
            <input type="submit" value="Save">
        </form>
    </div>
    <div id="table">
        <table>
            <thead>
		<th>Email</th>
            	<th>Category</th>
            	<th>Title</th>
            	<th>Description</th>
            </thead>
            <tbody>
                <?php
		    $mysqli = new mysqli('db', 'root', 'helloworld', 'web');

		    if (mysqli_connect_errno()) {
			printf('Подключение к серверу MySQL невозможно. Код ошибки: %s\n', mysqli_connect_error());
			exit;
		    }
		    if ($result = $mysqli->query('SELECT * FROM ad ORDER BY created DESC')) {
			while ($row = $result->fetch_assoc()){ ?>
		            <tr>
			        <td><?php echo $row['email'];?></td>
				<td><?php echo $row['category'];?></td>
				<td><?php echo $row['title'];?></td>
				<td><?php echo $row['description'];?></td>
		            </tr>
		        <?php }
		    }
	 	?>
            </tbody>
        </table>
    </div>
</body>
</html>
