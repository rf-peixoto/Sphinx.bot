import re

class Tools:
    def __init__(self):
        self.client_id = 'BOT CLIENT ID'
        self.owner_id = 'BOT OWNER ID'
        self.bot_token = 'BOT TOKEN'
        self.trash = ['\r', '\n', '\t', '\0', "'", '"', '\\', '/', '&', '|', '#', '$', '%', '<', '>', '(', ')', '{', '}', ';', '*', '[', ']', '--', ' ']
        self.email_pattern = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    def sanitize(self, message, counter=3):
        tmp = message.split(" ")[0]
        for c in self.trash:
            if c in tmp:
                tmp = tmp.replace(c, '')
        counter -= 1
        if counter > 0:
            self.sanitize(tmp, counter)
        return tmp

    def check_string(self, string):
        if re.match(self.email_pattern, string):
            return True
        else:
            return False
