from pprint import pprint

def insert_db(data_csv):
    data = data_csv.split('\n')
    keys = tuple(data.pop(0).split(','))

    list1 = []
    for i in data:
        dic = {}
        values = i.split(',')
        for i,key in enumerate(keys):
            dic[key] = values[i]
        list1.append(dic)

    return list1

f = open('specifications.csv','r').read()
pprint(insert_db(f))