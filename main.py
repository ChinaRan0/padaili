import requests
import json
from urllib.parse import unquote

def main():
 
    print("正在爬取fofa数据")
    fofaurl = "https://fofa.info/api/v1/search/all?key=这里写你的fofakey&qbase64=cHJvdG9jb2w9PSJzb2NrczUiICYmICJWZXJzaW9uOjUgTWV0aG9kOk5vIEF1dGhlbnRpY2F0aW9uKDB4MDApIiAmJiBjb3VudHJ5PSJDTiI=&size=5000"
    fofares = requests.get(fofaurl)
    # print(fofares.text)
    data = json.loads(fofares.text)
    print("正在提取数据")
    # 从results中提取所有的IP地址和端口（索引0的元素）
    extracted_data = [result[0] for result in data['results']]

    with open('proxy.txt', 'w') as f:
        pass
    for it in extracted_data:
        with open('proxy.txt', 'a') as f:
            f.write(it + '\n')
    print("数据爬取完毕，proxy.txt文件已生成")


main()