# http://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p01_read_write_csv_data.htmlimport csv
import  csv
from collections import  namedtuple
import json
def readCsv():
    filePath="test.csv"
    with open(filePath,'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        # for index, row in enumerate(reader):
        #     if(index>0):
        #         print(row[0])

        heading = next(reader)
        row = namedtuple('row',heading)
        for r in reader:
            data = row(*r)
            print(data,data.Symbol)

def writeCSV():
    filePath = "test.csv"
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']

    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
            ]
    with open(filePath,'w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
def writeListCsv():
    filePath = "test_list.csv"
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']

    row = ['AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800]


    with open(filePath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerow(row)

def dictWriteCSV():
    filePath = "test_dict.csv"
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
            {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
            {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
            ]
    with open(filePath,'w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(rows)


def readJson():
    filePath = "myjson.json"
    # data = json.loads(json_str)  # convert a string to json data
    # json_str = json.dumps(data)  # conver json data to string
    with open(filePath,'r',encoding='utf-8') as f:
        data = json.load(f)
        for d in data:
            print(d, d["Symbol"])

def writeJson():
    filePath = "myjson.json"
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
            {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
            {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
            ]
    with open(filePath,'w',encoding='utf-8') as f:
        for r in rows:
            content = json.dumps(r,ensure_ascii=False)
            f.write(content+",\n")

# writeCSV()



 
# dictWriteCSV()
# readCsv()

# writeJson()
# readJson()

writeListCsv()