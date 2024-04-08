import time

import httpx
import asyncio

async def make_request(endpoint, data):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://dkjf.ujn.edu.cn',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://dkjf.ujn.edu.cn/wxapp/api?keyCode=pay&schoolCode=10427&from=groupmessage&isappinstalled=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    async with httpx.AsyncClient() as client:
        url = f'http://dkjf.ujn.edu.cn/wxapp/api/pay/{endpoint}'
        response = await client.post(url, headers=headers, data=data)
        return response.json()

async def query_building():
    data = {
        'selXq': '西校区',
        'selLx': '楼座',
        'selTj': '',
    }

    return await make_request('queryBuilding', data)

async def query_floor(building_id):
    data = {
        'selXq': '西校区',
        'selLx': '楼层',
        'selTj': building_id,
    }

    return await make_request('queryBuilding', data)

async def query_room(floor_id):
    data = {
        'selXq': '西校区',
        'selLx': '房间',
        'selTj': floor_id,
    }

    return await make_request('queryBuilding', data)

async def query_elec_bill(room_id):
    data = {
        'userXq': '西校区',
        'userFj': room_id,
        'payType': '2',
    }

    return await make_request('queryElectricity', data)

async def get_room_list():
    room_list = []
    buildings = await query_building()
    for building in buildings['message']:
        building_id = building.split(':')[0]
        floors = await query_floor(building_id)
        for floor in floors['message']:
            floor_id = floor.split(':')[0]
            rooms = await query_room(floor_id)
            for room in rooms['message']:
                room_id = room.split(':')[0]
                room_list.append(room_id)
    return room_list

async def main():
    # 读取room_list.json文件中的数据
    # file template:
    # ["101001", "101002"]
    with open('room_list.json', 'r') as f:
        room_list = f.read()
#     使用httpx的异步请求
    async with httpx.AsyncClient() as client:
        tasks = [client.get(f'http://dkjf.ujn.edu.cn/wxapp/api/pay/queryElectricity?userXq=西校区&userFj={room}&payType=2') for room in room_list]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result.json())



start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f'运行时间：{end_time - start_time}秒')

# D:\Project\Elec_spider\.venv\Scripts\python.exe D:\Project\Elec_spider\test2.py
# Traceback (most recent call last):
#   File "E:\ENV\Python310\lib\site-packages\httpcore\_synchronization.py", line 125, in wait
#     await self._anyio_event.wait()
#   File "E:\ENV\Python310\lib\site-packages\anyio\_backends\_asyncio.py", line 1778, in wait
#     if await self._event.wait():
#   File "E:\ENV\Python310\lib\asyncio\locks.py", line 214, in wait
#     await fut
# asyncio.exceptions.CancelledError
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "E:\ENV\Python310\lib\site-packages\httpcore\_exceptions.py", line 10, in map_exceptions
#     yield
#   File "E:\ENV\Python310\lib\site-packages\httpcore\_synchronization.py", line 124, in wait
#     with anyio.fail_after(timeout):
#   File "E:\ENV\Python310\lib\site-packages\anyio\_core\_tasks.py", line 119, in __exit__
#     raise TimeoutError
# TimeoutError
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "E:\ENV\Python310\lib\site-packages\httpx\_transports\default.py", line 60, in map_httpcore_exceptions
#     yield
#   File "E:\ENV\Python310\lib\site-packages\httpx\_transports\default.py", line 353, in handle_async_request
#     resp = await self._pool.handle_async_request(req)
#   File "E:\ENV\Python310\lib\site-packages\httpcore\_async\connection_pool.py", line 242, in handle_async_request
#     raise exc
#   File "E:\ENV\Python310\lib\site-packages\httpcore\_async\connection_pool.py", line 233, in handle_async_request
#     connection = await status.wait_for_connection(timeout=timeout)
#   File "E:\ENV\Python310\lib\site-packages\httpcore\_async\connection_pool.py", line 35, in wait_for_connection
#     await self._connection_acquired.wait(timeout=timeout)
#   File "E:\ENV\Python310\lib\site-packages\httpcore\_synchronization.py", line 123, in wait
#     with map_exceptions(anyio_exc_map):
#   File "E:\ENV\Python310\lib\contextlib.py", line 153, in __exit__
#     self.gen.throw(typ, value, traceback)
#   File "E:\ENV\Python310\lib\site-packages\httpcore\_exceptions.py", line 14, in map_exceptions
#     raise to_exc(exc) from exc
# httpcore.PoolTimeout
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "D:\Project\Elec_spider\test2.py", line 91, in <module>
#     asyncio.run(main())
#   File "E:\ENV\Python310\lib\asyncio\runners.py", line 44, in run
#     return loop.run_until_complete(main)
#   File "E:\ENV\Python310\lib\asyncio\base_events.py", line 649, in run_until_complete
#     return future.result()
#   File "D:\Project\Elec_spider\test2.py", line 84, in main
#     results = await asyncio.gather(*tasks)
#   File "E:\ENV\Python310\lib\site-packages\httpx\_client.py", line 1757, in get
#     return await self.request(
#   File "E:\ENV\Python310\lib\site-packages\httpx\_client.py", line 1530, in request
#     return await self.send(request, auth=auth, follow_redirects=follow_redirects)
#   File "E:\ENV\Python310\lib\site-packages\httpx\_client.py", line 1617, in send
#     response = await self._send_handling_auth(
#   File "E:\ENV\Python310\lib\site-packages\httpx\_client.py", line 1645, in _send_handling_auth
#     response = await self._send_handling_redirects(
#   File "E:\ENV\Python310\lib\site-packages\httpx\_client.py", line 1682, in _send_handling_redirects
#     response = await self._send_single_request(request)
#   File "E:\ENV\Python310\lib\site-packages\httpx\_client.py", line 1719, in _send_single_request
#     response = await transport.handle_async_request(request)
#   File "E:\ENV\Python310\lib\site-packages\httpx\_transports\default.py", line 352, in handle_async_request
#     with map_httpcore_exceptions():
#   File "E:\ENV\Python310\lib\contextlib.py", line 153, in __exit__
#     self.gen.throw(typ, value, traceback)
#   File "E:\ENV\Python310\lib\site-packages\httpx\_transports\default.py", line 77, in map_httpcore_exceptions
#     raise mapped_exc(message) from exc
# httpx.PoolTimeout
#
# 进程已结束,退出代码1
# 报错原因是？
# q: 为什么会出现这个错误？
# a: 由于httpx的连接池默认是10个，当并发请求超过10个时，就会出现连接池满的情况，这时候就会报错。
# q: 怎么解决这个问题？
# a: 有两种方法，一种是增加连接池的大小，另一种是减少并发请求的数量。
# q: 怎么增加连接池的大小？
# a: 在创建httpx.Client对象时，传入参数limits，如下所示：
# client = httpx.Client(limits=httpx.Limits(max_connections=100))
# q: 怎么减少并发请求的数量？
# a: 在asyncio.gather()中传入参数return_exceptions=True，如下所示：
# results = await asyncio.gather(*tasks, return_exceptions=True)
# q: 为什么减少并发请求的数量就能解决问题？
# a: 因为减少并发请求的数量，就不会出现连接池满的情况，也就不会报错了。