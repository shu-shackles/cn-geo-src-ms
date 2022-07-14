import csv
import time
import os
import requests


## 判断字符串是否是小数
def DataCheck():
  starttime = time.time()
  i = 0
  with open('address.csv') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
      longi = row[0]
      lati = row[1]

      if (longi.split(".")[0]).isdigit() and (lati.split(".")[0]).isdigit():
        None
      else:
        print(reader.line_num + 1, '行中的(', longi, ')(', lati, ")格式检查不通过，请修改后再试")
        i = i + 1
    if i == 0:
      print('经纬度检查完成，未发现错误')
    else:
      print('检查完成，发现错误', i, '个')
  endtime = time.time()


## 纠偏
## https://lbs.amap.com/api/webservice/guide/api/convert API链接
def recorrect(locationX):  # 纠偏API函数
  parameters = {'locations': locationX, 'key': 'c5668c9cdc12424a405008a713034dc4', 'coordsys': 'gps'}
  base_url = 'https://restapi.amap.com/v3/assistant/coordinate/convert'
  response = requests.get(url=base_url, params=parameters)
  info_newGPS = response.json()
  return info_newGPS['locations']


def split(lst):  # 数据按照二十个一组进行处理
  new_lst = []
  new = [lst[i:i + 20] for i in range(0, len(lst), 20)]
  i = 0
  for i in range(len(new)):
    # print('提取中: {:.0f}%'.format(i / len(new) * 100))
    a = "|".join(str(m) for m in new[i])
    new_lst.append(a)
  return new_lst


def DealData(lst):  # 分列后进行处理查询
  new_lst = split(lst)
  result_list = []
  new_result_combine = []
  for i in range(len(new_lst)):
    block1 = new_lst[i]
    # print('检查：',block1)
    result = recorrect(block1)
    # print('纠偏经纬度为：',result)
    result_list.append(result)
    # print('最终结果为：',result_list)
    new_result_combine = zip(result_list)
    # print(new_result_combine)
    new_result_list = list(new_result_combine)
    # print('转换结果：',new_result_list)
  return new_result_list


def RecorrectV4():
  starttime = time.time()
  lst = []
  with open('address.csv') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
      longi = row[0]
      lati = row[1]
      location = longi + ',' + lati
      lst.append(location)

  new_result_list = DealData(lst)

  with open('newGPS.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(new_result_list)
  endtime = time.time()


##获取地址
def lo_to_addr(location):  # 经纬度转地址
  parameters = {'location': location, 'key': 'c5668c9cdc12424a405008a713034dc4', 'batch': 'true'}
  base_url = 'https://restapi.amap.com/v3/geocode/regeo'
  response = requests.get(url=base_url, params=parameters)
  info_site = response.json()
  # 地区路径：info_site['regeocode']['addressComponent']['district']
  # 地址路径：info_site['formatted_address']
  return info_site['regeocodes']


def GetAddV4():
  starttime = time.time()

  with open('newGPS.csv') as f:
    reader = csv.reader(f)
    # for row in reader:
    #     # 行号从1开始
    #     print(reader.line_num, row)

    dis_from_location_list = []
    address_from_location_list = []
    longi_list = []
    lati_list = []
    location_list = []

    for row in reader:
      location = row[0]
      # print(location)
      location = location.replace(';', '|')
      result = lo_to_addr(location)

      for num in range(0, 20):
        try:
          DataPart = result[num]
        except IndexError:
          break
        addre = DataPart['formatted_address']
        dis = DataPart['addressComponent']['district']
        # print('检查:',DataPart)
        # print('地址:',addre)
        # print('地区:', dis)
        address_from_location_list.append(addre)
        dis_from_location_list.append(dis)
    # print(address_from_location_list)
    # print(dis_from_location_list)

    dis_from_location_list.insert(0, '地区')
    address_from_location_list.insert(0, '地址')

  result_combine = zip(dis_from_location_list, address_from_location_list)
  result_list = list(result_combine)
  with open('dis.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result_list)
  endtime = time.time()


def generateCSV(lon, lat):
  headers = ['longitude', 'latitude']
  rows = [(lon, lat)]
  with open('address.csv', 'w', encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)


def get_result():
  with open('dis.csv') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
      area = row[0]
      addr = row[1]
      return addr


# 主程序入口
def coords_to_city(lon, lat):
  generateCSV(lon, lat)
  DataCheck()
  RecorrectV4()
  GetAddV4()
  return get_result()
