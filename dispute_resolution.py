contract DisputeResolution:

    def __init__(self):
        self.disputes = {}
        self.counter = 0

    def raise_dispute(self, user, issue, severity):
        d_id = self.counter
        self.counter += 1

        self.disputes[d_id] = {
            "user": user,
            "issue": issue,
            "severity": severity,
            "status": "open"
        }

        return d_id

    def resolve(self, d_id):
        d = self.disputes[d_id]

        if d["severity"] > 7:
            d["result"] = "guilty"
        elif d["severity"] > 3:
            d["result"] = "warning"
        else:
            d["result"] = "dismissed"

        d["status"] = "closed"
        return d["result"]
