<?php
  $connection=mysqli_connect("localhost","root","","registeruser");
  if (mysqli_connect_errno())
    {
    echo 'NOT_OK';
    }

  mysqli_query($connection,"UPDATE articles SET amount = (amount + 1)
      WHERE id='1'");

  mysqli_close($connection);

  echo 'OK';   ?>