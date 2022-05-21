# utf-8
import requests
url = 'https://www.zhbch.org.cn/lvyou/'
strHTML = requests.get(url)
print(strHTML.text)
def search_words():
    # 保存搜索到的词
    words = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    for word in init_words:
        response = requests.get(url, headers=headers)
        # 对获取的源代码进行整理分析，通过Xpath定位需要的资源
        r = response.text
        html = etree.HTML(r, etree.HTMLParser())
        #r1 = html.xpath('/html[1]/body[1]/p[contains(text(),"旅游的近义词")]')
        r1 = html.xpath('/html[1]/body[1]//span')
        #r2 = html.xpath('//p[contains(text(),"旅游的相似词")]')
        # string(.)方法可以获取节点下所有嵌套节点内容
        #a = i.xpath('string(.)')
        #获取近义词sim1
        sim1 = []
        import re
        for i in r1:
            new = re.sub('[^\u4e00-\u9fa5]+', '', str(i.xpath('string(.)')))
            sim1.append(new)

        # 去除列表中的空元素
        while '' in sim1:
            sim1.remove('')
        # 将元素并入词典
        words += sim1

    return words
