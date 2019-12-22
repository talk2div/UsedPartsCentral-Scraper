"""
main_url = https://www.usedpartscentral.com/landingpage.php
makes = https://www.usedpartscentral.com/getmakes.php?year=2015
models = https://www.usedpartscentral.com/getmodels.php?year=2015&make=Acura
parts = https://www.usedpartscentral.com/getparts.php
"""
from lxml import html,etree
import requests
from fake_useragent import UserAgent
import csv
dictheaders = ['Year', 'Makes', 'Models', 'Parts']
ua = UserAgent()
headers = {
    'User-Agent':ua.random
}
resp = requests.get(url="https://www.usedpartscentral.com/landingpage.php",headers=headers)
tree = html.fromstring(html=resp.content)
year = tree.xpath("//select[@tabindex='1']/option/text()")[1:]

def getmakes(yrs):
    makresp = requests.get(url=f"https://www.usedpartscentral.com/getmakes.php?year={yrs}",headers=headers)
    maktree = html.fromstring(html=makresp.content)
    try :
        return maktree.xpath("//select[@tabindex='2']/option/text()")[1:]
    except IndexError:
        return ''

def getmodels(yrs,mks):
    modresp = requests.get(url=f"https://www.usedpartscentral.com/getmodels.php?year={yrs}&make={mks}",headers=headers)
    modtree = html.fromstring(html=modresp.content)
    try :
        return modtree.xpath("//select[@tabindex='3']/option/text()")[1:]
    except IndexError:
        return ''

def getparts():
    parresp = requests.get(url="https://www.usedpartscentral.com/getparts.php",headers=headers)
    partree = html.fromstring(html=parresp.content)
    try :
        return partree.xpath("//select[@tabindex='4']/option/text()")[1:]
    except IndexError:
        return ''
with open("usedpartscentral.csv", 'w') as f:
        writer = csv.DictWriter(f, dictheaders)
        writer.writeheader()
        for each_year in year:
            for mak in getmakes(each_year):
                for mod in getmodels(each_year,mak):
                    for par in getparts():
                        data = {
                            'Year': each_year, 
                            'Makes':mak, 
                            'Models':mod, 
                            'Parts':par
                        }
                        writer.writerow(data)
