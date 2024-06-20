import socket
import concurrent.futures

file_path = "proxy.txt"
open_proxies = []

# 测试端口是否开放的函数
def test_proxy(proxy):
    proxy = proxy.strip()  # 去除行尾的换行符
    ip, port = proxy.split(":")
    try:
        # 创建一个TCP socket连接
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # 设置超时时间为2秒

        # 尝试连接端口
        result = sock.connect_ex((ip, int(port)))

        # 如果端口开放，添加到开放代理列表
        if result == 0:
            open_proxies.append(proxy)

        sock.close()
    except socket.error:
        pass

# 读取文件
with open(file_path, "r") as f:
    proxies = f.readlines()

# 设置线程池数量为10
max_workers = 100

# 使用线程池测试端口
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    executor.map(test_proxy, proxies)

# 将开放的代理写入文件
with open("port_open.txt", "w") as f:
    f.write("\n".join(open_proxies))
