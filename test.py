# Encoding: utf-8


import json
import os
from datetime import datetime
from pathlib import Path

import requests
import httpx
def queryElec():

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://dkjf.ujn.edu.cn',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://dkjf.ujn.edu.cn/wxapp/api?keyCode=pay&schoolCode=10427&from=groupmessage&isappinstalled=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    # 27为楼号，02为楼层，001为房间号
    data = {
        'userXq': '西校区',
        'userFj': '2702001',
        'payType': '2',
    }
    response = requests.post(
        'http://dkjf.ujn.edu.cn/wxapp/api/pay/queryElectricity',
        headers=headers,
        data=data,
        verify=False,
    )
    return response.json()
# response.json()的返回值
# {
#   "success": true,
#   "message": {
#     "negElec": "0.00",
#     "freeElec": "0.00",
#     "room": "2702001",
#     "feeElec": "363.93",
#     "plusElec": "363.93",
#     "status": "正常供电"
#   }
# }

# 房间标识：{message["message"]["room"]}
# 免费电量：{message["message"]["freeElec"]}度
# 负值电量：{message["message"]["negElec"]}度
# 收费电量：{message["message"]["feeElec"]}度
# 剩余电量：{message["message"]["plusElec"]}度
# 供电状态：{message["message"]["status"]}''')



# json template
# {
#     "270201": [
#         {
#             "2022-06-19 13:57:19": "55.55"
#         },
# ]
# }
# path Path(os.getcwd()) / 'res' / 'ElecData.json'
# @scheduler.scheduled_job("cron", minute='*/15', id="job_0")
# 查询电费，每5分钟一次，按照格式储存到json文件
async def job_0():
    message = queryElec()
    # "status":"获取数据异常"
    if message["message"]["status"] == "获取数据异常":
        return

    path = Path(os.getcwd()) / 'res' / 'ElecData.json'
    if not path.exists():
        with open(path, 'w') as f:
            f.write(json.dumps({}))

    with open(path, 'r') as f:
        data = json.loads(f.read())
    if message["message"]["room"] not in data:
        data[message["message"]["room"]] = []
    data[message["message"]["room"]].append(
        {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"): message["message"]["plusElec"]})
    with open(path, 'w') as f:
        f.write(json.dumps(data))

# 使用httpx库，异步查询电费，每30分钟一次，按照格式储存到json文件
# 查询范围楼号：1~35，楼层:1~6，房间号:1~50
async def job_1():
    async with httpx.AsyncClient() as client:
        for i in range(1, 36):
            for j in range(1, 7):
                for k in range(1, 51):
                    data = {
                        'userXq': '西校区',
                        'userFj': f'{i}{j}{k}',
                        'payType': '2',
                    }
                    response = await client.post(
                        'http://dkjf.ujn.edu.cn/wxapp/api/pay/queryElectricity',
                        data=data,
                        verify=False,
                    )
                    message = response.json()
                    if message["message"]["status"] == "获取数据异常":
                        continue
                    path = Path(os.getcwd()) / 'res' / 'ElecData.json'
                    if not path.exists():
                        with open(path, 'w') as f:
                            f.write(json.dumps({}))
                    with open(path, 'r') as f:
                        data = json.loads(f.read())
                    if message["message"]["room"] not in data:
                        data[message["message"]["room"]] = []
                    data[message["message"]["room"]].append(
                        {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"): message["message"]["plusElec"]})
                    with open(path, 'w') as f:
                        f.write(json.dumps(data))
