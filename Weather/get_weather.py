"""
开发目标：
1.在每日的早上七点准时发送当日的天气情况 （主动Ark消息形式）
2.当频道成员使用@指令并指明天气时，就推动频道成员输入的参数城市
"""
import os
import aiohttp
from pprint import pprint
from qqbot.core.util.yaml_util import YamlUtil
from typing import Dict
import json
import asyncio


# 导入配置文件
test_config = YamlUtil.read(os.path.join(os.path.dirname(__file__), '../config.yaml'))
# 心知天气的api查询密钥
xinzhi_weather_api_key = "S62so4PCUs67fdG5a"

# 输入查询城市的天气


async def get_weather(data: str) -> Dict:
    weather_api_url = f'https://api.seniverse.com/v3/weather/now.json?key={xinzhi_weather_api_key}&location={data}&language=zh-Hans&unit=c'
    async with aiohttp.ClientSession() as session:
        async with session.get(
                url=weather_api_url,
                timeout=5,
        ) as resp:
            content = await resp.text()
            content_json_obj = json.loads(content)
            pprint(content_json_obj)
            return content_json_obj


if __name__ == '__main__':
    location = input("请输入你要查询的位置:")
    location_transfer = test_config['city'][location]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_weather(location_transfer))

