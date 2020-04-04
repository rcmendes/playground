from echo.echoing import echo


def test_echo_with_message():
    message = "Testing"
    assert message == echo(message)
