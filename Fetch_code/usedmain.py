"""

"""
from lxml import html,etree
import requests
from fake_useragent import UserAgent
import csv
ua = UserAgent()
headers = {
    'User-Agent':ua.random
}
subheaders = ['Main', 'SubMenu', 'URL', 'IMGURL','Description']
resp = requests.get(url="https://www.usedpart.us/",headers=headers)
tree = html.fromstring(html=resp.content)
usedpart = tree.xpath("//div[@class='left_nav']")[0]
part = usedpart.xpath(".//div[1]/ul[@id='menu-left_nev']/li/a/text()")
csv_file = open("main.csv", 'a',encoding="utf-8")
writer = csv.DictWriter(csv_file, subheaders)
writer.writeheader()
def get_check(img_list):
    try:
        return img_list[0]
    except IndexError:
        return 'IMAGE NOT PRESENT'
def send_data_to_csv(subpart,sublink,prt):
    for i in range(len(subpart)):
        sub_resp = requests.get(url=sublink[i],headers=headers)
        subtree = html.fromstring(html=sub_resp.content)
        data = {
            'Main':prt,
            'SubMenu':subpart[i],
            'URL':sublink[i],
            'IMGURL': get_check(subtree.xpath("//div[@class='fea_img']/img/@src")),
            'Description': b''.join(list(html.tostring(i) for i in subtree.xpath("//div[@class='midd_sec']/p")))
        }
        writer.writerow(data)



for i in range(2,len(part)):
    subpart = tree.xpath(f'.//div[1]/ul[@id="menu-left_nev"]/li[{i}]/ul/li/a/text()')
    sublink = tree.xpath(f'.//div[1]/ul[@id="menu-left_nev"]/li[{i}]/ul/li/a/@href')
    send_data_to_csv(subpart,sublink,part[i-1])

csv_file.close()