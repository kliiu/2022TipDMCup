# 搜索近义词并保存
import json
import requests
from lxml import etree

ori_dict = "旅游、节庆、特产、交通、酒店、景区、景点、文创、文化、乡村旅游、民宿、" \
  "假日、假期、游客、采摘、赏花、春游、踏青、 康养、公园、滨海游、度假、农家乐、剧本杀、" \
    "旅行、徒步、工业旅游、线路、自驾游、团队游、攻略、游记、包车、玻璃栈道、游艇、高尔夫、" \
    "温泉"
init_words = ori_dict.split("、")

# requests进行请求搜索

def search_words():
    # 保存搜索到的词
    words = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    for word in init_words:
        response = requests.get('https://kmcha.com/similar/'+word, headers=headers)
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


# 输出词表
init_words += search_words()
with open('words_dict.txt', 'w') as file_obj:
    for word in set(init_words):
        file_obj.write('\''+word+'\''+',')
        file_obj.read()
    file_obj.close()
"""
    #获取相似词sim2
    #a = r1[0].xpath('string(.)')
    # 将答案保存为字符串
    output = ''
    for i in a:
        output += str(i)
    # 按空格将答案分割为列表
    sim2 = output.split()
    # 保存至最终的列表
    #words += sim1
"""
