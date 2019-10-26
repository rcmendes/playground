<?php

namespace Core\Database;

use PDO;

class QueryBuilder
{
    private $connection;
    public function __construct(PDO $connection)
    {
        $this->connection = $connection;
    }
    public function fetchAll($table, $fields = [], $where_parameters = [], $limit = 0, $startIndex = 0)
    {
        $limit_values = "";
        if ($limit > 0) {
            $limit_values = "LIMIT $startIndex,$limit";
        }

        $fields_list = "";
        if (sizeof($fields) > 0) {
            foreach ($fields as $field) {
                $fields_list .= ", $field";
            }
            $fields_list = substr($fields_list, 2);
        } else {
            $fields_list = "*";
        }

        $where = "";

        $values = [];
        if (sizeof($where_parameters) > 0) {
            $where = "WHERE";

            foreach ($where_parameters as $field => $value) {
                $operator = "=";
                if (gettype($value) == 'string') {
                    $operator = "LIKE";
                }
                $where .= " $field $operator ? AND";
                $values[] = $value;
            }

            $where = substr($where, 0, strlen($where) - 4);
        }

        $query = "SELECT $fields_list FROM $table $where $limit_values";

        // echo "\n>" . $query . "\n";

        $stmt = $this->connection->prepare($query);

        $stmt->execute($values);

        return $stmt->fetchAll(PDO::FETCH_CLASS);
    }

    public function fetchOne($table, $fields = [], $where_parameters = [])
    {
        $fields_list = "";
        if (sizeof($fields) > 0) {
            foreach ($fields as $field) {
                $fields_list .= ", $field";
            }
            $fields_list = substr($fields_list, 2);
        } else {
            $fields_list = "*";
        }

        $where = "";

        $values = [];
        if (sizeof($where_parameters) > 0) {
            $where = "WHERE";

            foreach ($where_parameters as $field => $value) {
                $operator = "=";
                if (gettype($value) == 'string') {
                    $operator = "LIKE";
                }
                $where .= " $field $operator ? AND";
                $values[] = $value;
            }

            $where = substr($where, 0, strlen($where) - 4);
        }

        $query = "SELECT $fields_list FROM $table $where";

        // echo "\n>" . $query . "\n";

        $stmt = $this->connection->prepare($query);

        $stmt->execute($values);

        return $stmt->fetchObject();
    }

    public function insert($table, $fields_values)
    {
        $values = [];
        $fields = [];
        $wildcards = [];
        if (sizeof($fields_values) > 0) {
            foreach ($fields_values as $field => $value) {
                $fields[] = $field;
                $values[] = $value;
                $wildcards[] = "?";
            }
        }

        $query = "INSERT INTO $table(" . implode(",", $fields) . ") VALUES(" . implode(",", $wildcards) . ")";

        // echo "\n>" . $query . "\n";

        $stmt = $this->connection->prepare($query);

        return $stmt->execute($values);
    }
}
