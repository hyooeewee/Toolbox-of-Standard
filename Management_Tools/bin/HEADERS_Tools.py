import random
from time import sleep
import requests
import _thread

def IP_Pool():
    # entry = 'http://{}:{}@140.249.73.234:15043'.format("StandardsSpider", "StandardsSpider")
    # proxy = {'http': entry,'https': entry,}

    HTTP_IP = []
    HTTPS_IP = []
    count = 10  # 一次获取的IP数量
    HTTP_response = requests.get("http://zltiqu.pyhttp.taolop.com/getip?count=" + str(
        count) + "&neek=87070&type=1&yys=0&port=1&sb=*&mr=1&sep=6")
    HTTP_IP_List = HTTP_response.text.split("*")
    HTTP_IP_List = HTTP_IP_List[:-1]
    for i in range(len(HTTP_IP_List)):
        HTTP_IP_List[i] = HTTP_IP_List[i].replace(" ", "").replace("\r", "").replace("\n", "")
        resp = requests.get("https://www.baidu.com", proxies={"http": "http://" + HTTP_IP_List[i]})
        if resp.status_code == 200:
            HTTP_IP.append(HTTP_IP_List[i])
    sleep(2)
    HTTPS_response = requests.get("http://zltiqu.pyhttp.taolop.com/getip?count=" + str(
        count) + "&neek=87070&type=1&yys=0&port=2&sb=*&mr=1&sep=6")
    HTTPS_IP_List = HTTPS_response.text.split("*")
    HTTPS_IP_List = HTTPS_IP_List[:-1]
    for i in range(len(HTTPS_IP_List)):
        HTTPS_IP_List[i] = HTTPS_IP_List[i].replace(" ", "").replace("\r", "").replace("\n", "")
        resp = requests.get("https://www.baidu.com", proxies={"http": "http://" + HTTPS_IP_List[i]})
        if resp.status_code == 200:
            HTTPS_IP.append(HTTPS_IP_List[i])
    total_list = [HTTP_IP, HTTPS_IP]
    print(total_list)

    return total_list


def Random_headers():
    headers_list = [{
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'},
                    {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'},
                    {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'},
                    {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'}
                    ]
    num = len(headers_list)
    return headers_list[random.randint(0, num - 1)]


def Random_IP(IP_List):  # 返回一个二维LIST，0是HTTP的，1是HTTPS的
    HTTP_proxies_IP = IP_List[0][random.randint(0, len(IP_List[0]) - 1)]
    HTTPS_proxies_IP = IP_List[1][random.randint(0, len(IP_List[1]) - 1)]
    proxies = {
        "http": "http://" + HTTP_proxies_IP,
        "https": "https://" + HTTPS_proxies_IP
    }
    return proxies
if __name__ == '__main__':
    print(IP_Pool())