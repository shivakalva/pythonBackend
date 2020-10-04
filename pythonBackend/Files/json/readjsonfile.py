import json

with open("C:\\MySpace\\COMPLETED\\data.json") as f:
    content = json.load(f)
    # print(content)
    print(content['quiz']['sport'][q1])
