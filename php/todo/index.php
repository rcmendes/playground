<?php

require_once('core/bootstrap.php');

use Core\Database\DBConnection;
use Core\Database\QueryBuilder;

$connection = DBConnection::connect();

$builder = new QueryBuilder($connection);
$builder->insert('tasks', ["title" => "Title " . time(), "description" => "Description of task " . time()]);

$tasks = $builder->fetchAll('tasks');
foreach ($tasks as $task) {
    echo "\n\n\tID:" . $task->id . "\n\tTITLE: " . $task->title;
    $description = $task->description;
    if ($description != null) {
        echo "\n\tDESCRIPTION: " . $task->description;
    }
}

// echo "\ntest 2";
// $tasks = $builder->fetchAll('tasks', ['id, description'], ['id' => 6]);
// foreach ($tasks as $task) {
//     echo "\n\n\tID:" . $task->id . "\n\tTITLE: " . $task->title;
//     $description = $task->description;
//     if ($description != null) {
//         echo "\n\tDESCRIPTION: " . $task->description;
//     }
// }

// echo "\ntest 3";
// $tasks = $builder->fetchAll('tasks', [], [], 2);
// foreach ($tasks as $task) {
//     echo "\n\n\tID:" . $task->id . "\n\tTITLE: " . $task->title;
//     $description = $task->description;
//     if ($description != null) {
//         echo "\n\tDESCRIPTION: " . $task->description;
//     }
// }

echo "\ntest 4";
$task = $builder->fetchOne('tasks', [], ["id" => 5]);
echo "\n\n\tID:" . $task->id . "\n\tTITLE: " . $task->title;
$description = $task->description;
if ($description != null) {
    echo "\n\tDESCRIPTION: " . $task->description;
}
