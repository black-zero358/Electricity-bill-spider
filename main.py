import json
import time
from datetime import datetime

import requests


def queryBuilding(school):
    cookies = {
        'JSESSIONID': 'c3094f68-b24f-45ca-89d1-900c81aded89',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=c3094f68-b24f-45ca-89d1-900c81aded89',
        'Origin': 'http://dkjf.ujn.edu.cn',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://dkjf.ujn.edu.cn/wxapp/api?keyCode=pay&schoolCode=10427&from=groupmessage&isappinstalled=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'selXq': school,
        'selLx': '楼座',
        'selTj': '',
    }

    response = requests.post(
        'http://dkjf.ujn.edu.cn/wxapp/api/pay/queryBuilding',
        # cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    return response.json()


# response.json()的返回值
# {
#     "success": true,
#     "message": [
#         "1:1号楼",
#         "2:2号楼",
#         "3:3号楼",
#         "4:4号楼",
#         "5:5号楼",
#         "6:6号楼",
#         "7:7号楼",
#         "8:8号楼",
#         "9:9号楼",
#         "10:10号楼",
#         "11:11号楼",
#         "12:12号楼",
#         "13:13号楼",
#         "14:14号楼",
#         "15:15号楼",
#         "16:16号楼",
#         "17:17号楼",
#         "20:20号楼",
#         "21:21号楼",
#         "22:22号楼",
#         "23:23号楼",
#         "24:24号楼",
#         "25:25号楼",
#         "27:27号楼",
#         "28:28号楼",
#         "30:30号楼",
#         "32:32号楼",
#         "33:33号楼",
#         "34:34号楼",
#         "35:35号楼"
#     ]
# }

def queryFloor(building_id):
    cookies = {
        'JSESSIONID': 'c3094f68-b24f-45ca-89d1-900c81aded89',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=c3094f68-b24f-45ca-89d1-900c81aded89',
        'Origin': 'http://dkjf.ujn.edu.cn',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://dkjf.ujn.edu.cn/wxapp/api?keyCode=pay&schoolCode=10427&from=groupmessage&isappinstalled=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'selXq': '西校区',
        'selLx': '楼层',
        'selTj': f'{building_id}',
    }

    response = requests.post(
        'http://dkjf.ujn.edu.cn/wxapp/api/pay/queryBuilding',
        # cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    return response.json()


# response.json()的返回值
# {
#     "success": true,
#     "message": [
#         "2701:01层",
#         "2702:02层",
#         "2703:03层",
#         "2704:04层",
#         "2705:05层",
#         "2706:06层"
#     ]
# }

def queryRoom(floor_id):
    cookies = {
        'JSESSIONID': 'c3094f68-b24f-45ca-89d1-900c81aded89',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=c3094f68-b24f-45ca-89d1-900c81aded89',
        'Origin': 'http://dkjf.ujn.edu.cn',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://dkjf.ujn.edu.cn/wxapp/api?keyCode=pay&schoolCode=10427&from=groupmessage&isappinstalled=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'selXq': '西校区',
        'selLx': '房间',
        'selTj': f'{floor_id}',
    }

    response = requests.post(
        'http://dkjf.ujn.edu.cn/wxapp/api/pay/queryBuilding',
        # cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    return response.json()


# response.json()的返回值
# {
#     "success": true,
#     "message": [
#         "2702001:2001号房间",
#         "2702002:2002号房间",
#         "2702003:2003号房间",
#         "2702004:2004号房间",
#         "2702005:2005号房间",
#         "2702006:2006号房间",
#         "2702007:2007号房间",
#         "2702008:2008号房间",
#         "2702009:2009号房间",
#         "2702010:2010号房间",
#         "2702011:2011号房间",
#         "2702012:2012号房间",
#         "2702013:2013号房间",
#         "2702014:2014号房间",
#         "2702015:2015号房间",
#         "2702016:2016号房间",
#         "2702017:2017号房间",
#         "2702018:2018号房间",
#         "2702019:2019号房间",
#         "2702020:2020号房间",
#         "2702021:2021号房间",
#         "2702022:2022号房间",
#         "2702023:2023号房间",
#         "2702024:2024号房间",
#         "2702025:2025号房间",
#         "2702026:2026号房间",
#         "2702027:2027号房间",
#         "2702029:2029号房间",
#         "2702031:2031号房间",
#         "2702050:2050号房间"
#     ]
# }

def queryElecBill(room_id):
    response = requests.post(
        f'http://dkjf.ujn.edu.cn/wxapp/api/pay/queryElectricity?userXq=西校区&userFj={room_id}&payType=2',
    )
    return response.json()


# response.json()的返回值
# {
#     "success": true,
#     "message": {
#         "negElec": "0.00",
#         "freeElec": "0.00",
#         "room": "2702001",
#         "feeElec": "281.56",
#         "plusElec": "281.56",
#         "status": "正常供电"
#     }
# }

# 根据上面的返回值，组合出所有楼栋，所有楼层，所有房间查询电费所需的参数
def room_list(school):
    params = []
    for building in queryBuilding(school)['message']:
        for floor in queryFloor(building.split(':')[0])['message']:
            for room in queryRoom(floor.split(':')[0])['message']:
                params.append(
                    room.split(':')[0]
                )
    return params

def getelecdata():
    with open('room_list.json', 'r') as f:
        room_list = eval(f.read())
    #     读取elec_bill.json现有数据，追加写入新数据
    with open('elec_bill.json', 'r') as f:
        elec_bill = json.loads(f.read())
    for room in room_list[0:6]:
        # 如果room_id不在elec_bill.json中，就添加
        if room not in elec_bill.keys():
            elec_bill[room] = []
            elec_bill[room].append(
                {
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'): queryElecBill(room)['message']['plusElec']
                }
            )
        else:
            elec_bill[room].append(
                {
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'): queryElecBill(room)['message']['plusElec']
                }
            )

    with open('elec_bill.json', 'w') as f:
        f.write(json.dumps(elec_bill, indent=4, ensure_ascii=False))

def save_room_list():
    school_list=["西校区","东校区","东校区校医院","东校区青年公寓"]
#     调用room_list()函数，获取所有校区房间号，并存储到不同的json文件中
    for school in school_list:
        with open(f'{school}.json', 'w') as f:
            f.write(json.dumps(room_list(school), indent=4, ensure_ascii=False))



# 记录代码运行时间
start_time = time.time()
save_room_list()
end_time = time.time()
print(f'运行时间：{end_time - start_time}秒')
