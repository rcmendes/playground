<?php
abstract class Model
{
    private $builder;
    public function __construct()
    {
        $connection = DBConnection::connect();
        $this->builder = new QueryBuilder($connection);
    }
    public function save()
    { }
}
