<?php 
  $flag="hkcert23{fakeflag1}";
  if(isset($_SERVER['HTTP_ENV']) && md5($flag.$_SERVER['HTTP_ENV']) == 0){
  	putenv($_SERVER['HTTP_ENV']);
  	include_once('index.php');
  }
?>