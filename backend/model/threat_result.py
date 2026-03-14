class ThreatResult:

    def __init__(self, target, threat_score, severity, message):
        self.target = target
        self.threat_score = threat_score
        self.severity = severity
        self.message = message

    def to_dict(self):
        return {
            "target": self.target,
            "score": self.threat_score,
            "severity": self.severity,
            "message": self.message
        }