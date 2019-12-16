from alert import Alert

class AlertList:

    def __init__(self, alerts):
        self.alerts = alerts
        self.organise()

    def organise(self):
        temp = {}
    
        # creates a dictionary where the key is the user id
        # and the value is the alert

        for alert in self.alerts:
            text = str(alert.text).lower()
            if alert.user_id not in temp:
                temp[alert.user_id] = [text]
            else:
                temp[alert.user_id].append(text)
        self.alerts = temp

    def search_list(self, nodelist):
        result = []

        for user_id, alerts in self.alerts.items():
            
            nodes = []

            for alert in alerts:    
                nodes_found = nodelist.search_list(alert)

                if nodes_found:
                    nodes.extend(nodes_found)

            result.append([user_id, nodes])

        return result
        
