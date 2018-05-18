import os, os.path, pickle, requests

def getImage(name, url):
    try:
        res = requests.get(url)
        if res.content:
            saveImage(res.content, name)
        raise Exception()
    except Exception as e:
        error.append([name, url])
        print('错误:<name:%s><url:%s>'%(name, url))
        return False

def saveImage(data, name):
    with open('./img/%s'%name, 'rb') as f:
        f.write(data)
        print('保存图片: %s'%name)

def crawlImage(preName, urls):
    for index, url in enumerate(urls):
        name = '%s-%d.png'%(preName, index+1)
        data = getImage(name, url)
    print('爬取图片结束')

def loadFile(file):
    with open(file, 'rb') as f:
        print('从文件%s加载数据'%file)
        return pickle.load(f)
    print('加载文件%s失败'%file)

def saveError(file, obj):
    if not obj:
        print('全部图片爬取成功，删除文件%s'%file)
        return
    with open(file, 'rb') as f:
        pickle.dump(obj, f)
        print('保存失败URL数据到文件%s'%file)

if __name__ == '__main__':
    error = []
    if not os.path.isfile('png_2.error'):
        # [[name1, [url1, url2]], 
        #  [name2, [url3, url4]]]
        imgUrls = loadFile('png_1.pkl')
        for record in imgUrls:
            crawlImage(*record)
    else:
        # [[name1, url1],
        #  [name2, url2]]
        imgUrls = loadFile('png_2.error')
        for item in imgUrls:
            getImage(*item)
    saveError('png_2.error', error)
