<?php

require_once('core/bootstrap.php');

use Core\Helpers\Router;

$path = "/contexto/123/detalhes/abc/complemento/xyz";
$path2 = "/contexto/123/detalhes/abc/complemento";
$pattern = "/contexto/:var1/detalhes/:var2/complemento/:var3";


$router = new Router();

$_SERVER["PATH_INFO"] = "/contexto/123/detalhes/abc/complemento/xyz";
$_SERVER["REQUEST_METHOD"] = "GET";

$router->get("/contexto/users/:id", "UserController@index");
$router->get("/contexto/:var1/detalhes/:var2/complemento/:var3", "UserController@index3");

$router->handle();
