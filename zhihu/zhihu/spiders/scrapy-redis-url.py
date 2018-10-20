import redis
from scrapy.utils.project import get_project_settings



settings = get_project_settings()
redis_client = redis.Redis(host=settings.get('REDIS_IP'), port=settings.get('REDIS_PORT'),password=settings.get('REDIS_PWD'),decode_responses=True)
# decode_responses=True，写入的键值对中的value为str类型，为 False 写入的则为字节类型，默认为False。


# 验证 重复的url ，已经爬取过的url
def validate_url(links):
    re_links = []
    for link in links:
        if not redis_client.sismember('urls', link.url):
            re_links.append(link)
        # 过滤掉已经存在的 url
        else:
            print('重复的url', link.url)

    return re_links