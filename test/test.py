urls = [
    'http://www.redis.cn/',
    'https://github.com',
    'http://www.runoob.com/',
    'http://baidu.com',
    'http://yahoo.com',
]

import time
import requests

from tomorrow import threads

@threads(5)
def download(url):
    return requests.get(url)

if __name__ == "__main__":

    start = time.time()
    responses = [download(url) for url in urls]
    html = [response.text for response in responses]
    end = time.time()
    print ("Time: %f seconds" % (end - start))