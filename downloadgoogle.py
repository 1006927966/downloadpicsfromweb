from urllib.parse import quote
import re
import requests

url = "https://www.google.com/search?q=%E7%BB%B4%E5%B0%BC%E7%86%8A&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjUqNSThJr1AhXY62EKHR05CA8Q_AUoAXoECAIQAw&biw=764&bih=745&dpr=2"
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}
html = requests.get(url, headers=headers)
html.encoding = 'utf-8'
html = html.text
#print(type(html))
#print(html)
pic_urls = re.findall(r'', html)
for pic in pic_urls:
    print(pic)