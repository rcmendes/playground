<?php

namespace Core\Helpers;

class RequestHandler
{

    public static function method()
    {
        return $_SERVER["REQUEST_METHOD"];
    }

    public static function uri()
    {
        return $_SERVER["REQUEST_URI"];
    }

    public static function contextPath()
    {
        return $_SERVER["PATH_INFO"];
    }

    public static function pathInfo()
    {
        return $_SERVER["PATH_INFO"];
    }

    public static function contentType()
    {
        return $_SERVER["HTTP_CONTENT_TYPE"];
    }

    public static function getQueryParamAsInt($param)
    {
        return intval($_REQUEST($param));
    }

    public static function getQueryParamAsBoolean($param)
    {
        return boolval($_REQUEST($param));
    }

    public static function getQueryParamAsString($param)
    {
        return $_REQUEST($param);
    }

    public static function getQueryParamAsDouble($param)
    {
        return doubleval($_REQUEST($param));
    }

    public static function getJsonBody()
    {
        $json = file_get_contents('php://input');

        return json_decode($json);
    }

    private static function getValues($source, $pattern)
    {
        $source_split = explode("/", $source);

        $pattern_split = explode("/", $pattern);

        $vars = [];
        foreach ($pattern_split as $index => $pathVar) {
            if (strlen($pathVar) > 0 && $pathVar{
                0} == ":") {
                $vars[substr($pathVar, 1)] = $source_split[$index];
            }
        }

        return $vars;
    }

    public static function getPathParams($pattern)
    {
        $source = $_SERVER["PATH_INFO"];
        return RequestHandler::getValues($source, $pattern);
    }

    public static function getPathParam($pattern, $param)
    {
        return RequestHandler::getPathParams($pattern)[$param];
    }
}
