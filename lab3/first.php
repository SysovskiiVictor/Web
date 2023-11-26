<?php
$myfile = fopen("testfile.txt", "a+");

$name = $_POST['name']."\n";
fwrite($myfile, $name);

$surname = $_POST['surname']."\n";
fwrite($myfile, $surname);

$email = $_POST['email']."\n";
fwrite($myfile, $email);

$report = $_POST['back']."\n";
fwrite($myfile, $back);

fclose($myfile);
?>