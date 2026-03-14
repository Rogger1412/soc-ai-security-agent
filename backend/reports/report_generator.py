import json
from datetime import datetime

def generate_report(data):

    filename = f"report_{datetime.now().timestamp()}.json"

    with open(filename,"w") as f:
        json.dump(data,f,indent=4)

    return filename