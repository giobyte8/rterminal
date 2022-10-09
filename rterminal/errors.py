
class BotAuthHashUndefinedError(Exception):
    def __init__(self):
        Exception.__init__(
            self,
            'BOT_AUTH_HASH env variable is undefined'
        )

class UnprocessableTelegramUpdateError(Exception):
    def __init__(self, msg: str):
        Exception.__init__(
            self,
            msg
        )
