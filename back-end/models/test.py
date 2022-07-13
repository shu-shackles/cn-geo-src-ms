import json
import requests

"""url = "http://mnr.gov.cn/dt/ywbb/"
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text"""

asd = ['2022-07-01', './202207/t20220701_2740919.html', '陈一新：决不允许利用“养老房”坑骗老年人']


if __name__ == "__main__":
    if asd[2].find("联合国") != -1 and not asd[1].startswith("./"):
        print("123")
    print("233")
