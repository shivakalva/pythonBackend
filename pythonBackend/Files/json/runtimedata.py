import json

with open("C:\\MySpace\\COMPLETED\\datas.json") as p:
    content = json.load(p)
    for check in content['checks']:
        if check['streetAddress'] == '127':
            print(check['city'])
            assert check['city'] == 'San Jone'

#######Comparing the 2 json file #######################

with open("C:\\MySpace\\COMPLETED\\data.json") as f:
    cont = json.load(f)
    assert content == cont
