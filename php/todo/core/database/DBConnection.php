<?php

namespace Core\Database;

use PDO;

class DBConnection
{
    public static function connect()
    {
        $dsn = getenv('DB_DIALECT') . ":host=" . getenv('DB_HOSTNAME') . ";dbname=" . getenv('DB_NAME');
        $username = getenv('DB_USERNAME');
        $password = getenv('DB_PASSWORD');
        $options = [
            PDO::ATTR_EMULATE_PREPARES   => false, // turn off emulation mode for "real" prepared statements
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, //turn on errors in the form of exceptions
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, //make the default fetch be an associative array
        ];

        return new PDO($dsn, $username, $password, $options);
    }
}
