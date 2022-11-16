import json
from urllib.request import urlopen


#url não funcionando
def getCountry(ipAddress):
    res = urlopen('http://freegeoip.net/json/'+ipAddress).read()
    res_json = json.loads(res)

    return res_json.get('country_code')

#print(getCountry('50.78.253.58'))

jsonString = '''
            {
                "arrayOfNums":[{"number":0},{"number":1},{"number":2}],
                "arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]
            }
            '''

jsonObj = json.loads(jsonString)

print(jsonObj.get('arrayOfNums'))
print(jsonObj.get('arrayOfNums')[1])
print(jsonObj.get('arrayOfFruits')[0].get('fruit'))
