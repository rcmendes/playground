<?php

$config = [
    "database" => [
        "hostname" => "127.0.0.1",
        "name" => "todo_dev",
        "port" => 3306,
        "username" => "dev",
        "password" => "d3v",
        "options" => [
            PDO::ATTR_EMULATE_PREPARES   => false, // turn off emulation mode for "real" prepared statements
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, //turn on errors in the form of exceptions
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, //make the default fetch be an associative array
        ]
    ]
];

set_exception_handler(function ($e) {
    error_log($e->getMessage());
    exit('\nSomething weird happened'); //something a user can understand
});

$dsn = "mysql:host=" . $config['database']['hostname'] . ";dbname=" . $config['database']['name'];
$username = $config['database']['username'];
$password = $config['database']['password'];
$options = $config['database']['options'];

$pdo = new PDO($dsn, $username, $password, $options);

$stmt = $pdo->prepare("INSERT INTO tasks(title) VALUES(?)");
$stmt->execute(["Title 1"]);
