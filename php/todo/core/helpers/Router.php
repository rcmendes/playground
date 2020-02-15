<?php

namespace Core\Helpers;

use Exception;

class Router
{
    private $routes = [
        "GET" => [],
        "POST" => [],
        "PUT" => [],
        "DELETE" => []
    ];

    public function get($path, $handler)
    {

        $method = $this->routes["GET"];
        if (!in_array($path, $method, true)) {
            $this->routes["GET"][$path] = $handler;
        }
    }

    public function handle()
    {

        $pathInfo = RequestHandler::contextPath();
        print_r("\n$pathInfo");
        $handlers = $this->routes[RequestHandler::method()];
        foreach ($handlers as $pattern => $handler) {
            $match = $this->matchPath($pathInfo, $pattern);

            print_r("\n\t$pattern | " . ($match ? "TRUE" : "FALSE"));

            if ($match) {
                $this->callMethod(...explode("@", $handler));
            }
        }
    }

    private function callMethod($controller, $method)
    {
        $controller = "App\\Controllers\\{$controller}";

        $instance = new $controller;
        if (!method_exists($controller, $method)) {
            throw new Exception("Method: '$method' on Controller '$controller' was not found.");
        }
        $instance->$method();
        //TODO create a Request class to manage request parameters and body

    }

    public function matchPath($path, $pattern)
    {
        $pattern_split = explode("/", $pattern);

        foreach ($pattern_split as $index => $pathVar) {
            if (strlen($pathVar) > 0 && $pathVar{
                0} == ":") {
                $pattern_split[$index] = "[\w]+";
            }
        }

        $regExp = "/" . implode("\/", $pattern_split) . "$/";

        preg_match($regExp, $path, $result);

        return sizeof($result) == 1;
    }
}
