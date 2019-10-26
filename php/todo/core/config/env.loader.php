<?php

namespace Core\Config;

$fn = fopen(".env", "r");

while (!feof($fn)) {
    $result = fgets($fn);
    if ($result[0] != '#') {
        $parameter = explode('=', $result);
        if (sizeof($parameter) == 2) {
            putenv(trim($parameter[0]) . "=" . trim($parameter[1]));
        }
    }
}

fclose($fn);
