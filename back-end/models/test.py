import json

if __name__ == "__main__":
    result = '{\n"result": "'+"成功"+'"\n}'
    result=json.loads(result)
    print(result)
