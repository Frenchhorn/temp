import pickle, os, os.path
from requests_html import HTMLSession

def getRecords(file):
    records = []
    with open(file, 'r') as f:
        for line in f.readlines():
            records.append(line.strip().split(','))
    print('总共 %d 条数据'%len(records))
    return records

def getUrls(url, name):
    urlList = []
    print('正在爬取<url:%s>'%url)
    try:
        res = session.get(url)
        res.html.render()
        for img in res.html.find('img'):
            urlList.append(img.attrs.get('src'))
    except Exception as e:
        print('错误:<name:%s><url:%s>'%(name, url))
        error.append([name, url])
        return False
    return [name, urlList]

def getImgUrls(records):
    imgUrls = []
    for record in records:
        name = record[0]+'-1'
        urlList = getUrls(record[1], name)
        if urlList:
            imgUrls.append(urlList)
        name = record[0]+'-2'
        urlList = getUrls(record[2], name)
        if urlList:
            imgUrls.append(urlList)
    print('爬取结束，总共 %d 条数据'%len(imgUrls))
    return imgUrls

def saveData(file, obj):
    with open(file, 'rb') as f:
        pickle.dump(obj, f)
        print('保存图片URL数据到文件%s'%file)

def saveError(file, obj):
    if not obj:
        os.remove(file)
        print('全部URL获取成功，删除文件%s'%file)
        return
    with open(file, 'rb') as f:
        pickle.dump(obj, f)
        print('保存失败URL数据到文件%s'%file)

if __name__ == '__main__':
    session = HTMLSession()
    error = []
    if not os.path.isfile('png_1.error'):
        records = getRecords('test.csv')
        # [[name1, urlList1], [name2, urlList2]]
        imgUrls = getImgUrls(records)
    else:
        with open('png_1.error', 'rb') as f:
            records = pickle.load(f)
        with open('png_1.pkl', 'rb') as f:
            imgUrls = pickle.load(f)
        for item in records:
            urlList = getUrls(url=item[1], name=item[0])
            if urlList:
                imgUrls.append(urlList)
    saveData('png_1.pkl', imgUrls)
    saveError('png_1.error', error)