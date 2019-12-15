from alert import Alert

class AlertList:

    def __init__(self, alerts):
        self.alerts = alerts
        self.organise()

    def organise(self):
        temp = {}
    
        # creates a dictionary where the key is the alert string
        # and the value is a list of users with that alert
        # this prevents the alert being searched for more than once
        # even if multipleusers have the same alert

        for alert in self.alerts:
            text = str(alert.text).lower()
            if text not in temp:
                temp[text] = [alert.user_id]
            else:
                temp[text].append(alert.user_id)
        self.alerts = temp

    def search_list(self, nodelist):
        result = []

        for alert, user_ids in self.alerts.items():
            nodes = nodelist.search_list(alert)

            if nodes:
                result.append([nodes, user_ids])

        return result
        
