import re

class Utils:
    def __init__(self):
        self.client_id = 'BOT CLIENT ID'
        self.owner_id = 'YOUR PERSONAL DISCORD ID'
        self.bot_token = 'BOT TOKEN'
        self.trash = ['\r', '\n', '\t', '\0', '\'', '\"', '\\', '&', '|', '#', '$', '%', '<', '>', '(', ')', '{', '}', ';', '*', '[', ']']
        self.email_pattern = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    def sanitize(self, message):
        tmp = message
        for c in self.trash:
            if c in message:
                tmp.replace(c, '')
        return tmp

    def check_string(self, string):
        if re.match(self.email_pattern, string):
            return True
        else:
            return False
