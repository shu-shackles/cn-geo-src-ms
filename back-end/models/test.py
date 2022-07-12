import json
import requests

url = "https://geocloud.cgs.gov.cn/#/geoscienceProducts/geoscienceProductsDetail?child_id" \
      "=cpgl_dzcp_8a8889b96e107a07016e125a5b5f01d8&yjlb=dxkp "
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text


if __name__ == "__main__":
    print(html)
