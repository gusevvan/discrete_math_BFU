<?php

function redirectToHome(): void 
{
    header('Location: /');

    exit();
}

if (false === isset($_POST['email'], $_POST['category'], $_POST['title'], $_POST['description'])) {
    redirectToHome();
}

$email = $_POST['email'];
$category = $_POST['category'];
$title = $_POST['title'];
$desc = $_POST['description'];

$mysqli = new mysqli('db', 'root', 'helloworld', 'web');

if (mysqli_connect_errno()) {
    printf('Подключение к серверу MySQL невозможно. Код ошибки: %s\n', mysqli_connect_error());
    exit;
} else {
    $mysqli->query("INSERT INTO ad (email, title, description, category) VALUES('$email', '$title', '$desc', '$category')");
}

redirectToHome();

