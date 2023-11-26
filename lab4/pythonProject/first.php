<?php

$servername = 'lab4';
$username = 'root';
$password = '';
$dbname = 'lab4';

// Подключение к БД
$conn = mysqli_connect($servername, $username, $password, $dbname);

$conn->set_charset("utf8mb4");

// Проверка подключения к БД
if(!$conn){
  die("Ошибка подключения". mysqli_connect_error());
} 

$name = $_POST['name'];
$surname = $_POST['surname'];
$patronymic = $_POST['patronymic'];
$phone_number = $_POST['phone_number'];
$email = $_POST['email'];
if (isset($_POST['shopping'])) {
  $shopping = $_POST['shopping'];
} else {
  $shopping = [];
}
$address = $_POST['address'];
$comment = $_POST['comment'];


$sql = "INSERT INTO `MyOrder` (`name`, `surname`, `patronymic`, `phone_number`, `email`, `shopping`, `address`, `comment`) VALUES (?,?,?,?,?,?,?,?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ssssssss", $name, $surname, $patronymic, $phone_number, $email, $shopping, $address, $comment);
$stmt->execute();

// header('Location: /');
?>