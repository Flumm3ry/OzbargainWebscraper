class User:
    def __init__(self, details):
        self.id = details[0]
        self.username = details[1]
        self.email = details[2]
        self.last_alert_checked = details[3]
