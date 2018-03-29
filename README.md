# Botengine.ai Python SDK (beta)

Overview
--------

The botengine.ai Python SDK makes it easy to communicate with the botengine agent (only supports text responses)

Prerequsites
--------
You need to have an botengine.ai account. Visit [Botengine.ai](https://www.botengine.ai/)


Usage examples
--------
Create an agent at [Botengine.ai](https://www.botengine.ai/) and get the developer access token

-Sending a query message

    >>> from botengine import BotEngine
    >>> botai = BotEngine(<DEVELOPER_ACCESS_TOKEN>)
    >>> request = botai.message()
    >>> request.query = "Hello"       #Query message
    >>> response = request.getresponse()
    ...

-Invoking a trigger

    >>> from botengine import BotEngine
    >>> botai = BotEngine(<DEVELOPER_ACCESS_TOKEN>)
    >>> request = botai.trigger()
    >>> request.name = "welcome"      #Trigger name
    >>> response = request.getresponse()
    ...

Documentation
-------------
Documentation is available at http://botengine.ai

## License
See [LICENSE](LICENSE).
