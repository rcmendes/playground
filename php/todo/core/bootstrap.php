<?php

namespace Core;

require_once('config/env.loader.php');

set_exception_handler(function ($e) {
    error_log($e->getMessage());
    die('Something went wrong. :( Sorry for the inconvenience and please, try later.');
});

spl_autoload_extensions(".php");
spl_autoload_register(function ($class) {
    require_once(str_replace('\\', '/', $class . '.php'));
});
