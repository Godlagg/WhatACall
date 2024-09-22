<?php
require_once('db.php');
$login = $_POST['login'];
$pass = $_POST['pass'];
$repeatpass = $_POST['repeatpass'];
$email = $_POST['email'];

if (empty($login) || empty($pass) || empty($repeatpass) || empty($email)){
    echo 'Заполните все поля';
}

      if($pass != $repeatpass){
        echo "Пароли не совпадают";
      }
    else{
        $sql = "INSERT INTO `users` (login,pass,email) VALUES('$login', '$pass', '$email')";

        if ($conn -> query($sql)===TRUE){
        echo 'Succesful';
        header ('Location: tggame.html');
        }
        else {
        echo "Ошибка:" .  $conn->error;
        }
    }
