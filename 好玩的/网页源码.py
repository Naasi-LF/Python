import requests
from bs4 import BeautifulSoup

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# 输入需要爬取的文档 URL
url = input("请输入需要爬取的文档 URL：")

# 发送 GET 请求
response = requests.get(url, headers=headers)

# 使用 BeautifulSoup 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 打印文档内容
print(soup.prettify())
