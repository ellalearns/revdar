import requests
from bs4 import BeautifulSoup

page = requests.get("https://play.google.com/store/apps/details?id=fm.castbox.audiobook.radio.podcast")

bs = BeautifulSoup(page.content, "html.parser")

reviews = bs.find_all("section")

try:
    if reviews == []:
        print("it's nothing")
    else:
        # for x in reviews:
        #     print("2")
        #     if "h3YV2d" in x:
        #         print(x)
        
        print(reviews[2].find_all("div")[78])
        # print(reviews[2].find_all("div")[0])
except:
    print("connection error")


#print(reviews[2].find_all("div")[40]) 
# found this "5,154 reviews for star rating 3"