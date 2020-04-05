# import json
# import urllib3
# import requests 
# from bs4 import BeautifulSoup 
import random

# # Trending Hashtags
# URL_en = "http://best-hashtags.com/hashtag/coronavirus/"
# URL_tn = "http://best-hashtags.com/hashtag/tamil/"
# URL_te = "http://best-hashtags.com/hashtag/telugu/"
# URL_mn = "http://best-hashtags.com/hashtag/malayali/"
# URL_bn = "http://best-hashtags.com/hashtag/bengali/"

# r_en = requests.get(URL_en) 
# r_tn = requests.get(URL_tn) 
# r_te = requests.get(URL_te) 
# r_mn = requests.get(URL_mn) 
# r_bn = requests.get(URL_bn) 

# soup_en = BeautifulSoup(r_en.content, 'html.parser') 
# soup_tn = BeautifulSoup(r_tn.content, 'html.parser') 
# soup_te = BeautifulSoup(r_te.content, 'html.parser') 
# soup_mn = BeautifulSoup(r_mn.content, 'html.parser') 
# soup_bn = BeautifulSoup(r_bn.content, 'html.parser') 

# hashtag_en = soup_en.find('p1').getText()
# hashtag_tn = soup_tn.find('p1').getText()
# hashtag_te = soup_te.find('p1').getText()
# hashtag_mn = soup_mn.find('p1').getText()
# hashtag_bn = soup_bn.find('p1').getText()

# print(hashtag_en)
# print(hashtag_tn)
# print(hashtag_te)
# print(hashtag_mn)
# print(hashtag_bn)

# # Statistics
# http = urllib3.PoolManager()
# r = http.request('GET', 'https://api.covid19india.org/data.json')
# data =  json.loads(r.data.decode('utf-8'))
# states = data["statewise"]
# for state in states:
#     if(state["state"] == "Total"):
#         stats = "Statistics in India\nConfirmed: "+state["confirmed"]+"\nActive: "+state["active"]+"\nRecovered: "+state["recovered"]+"\nDeaths: "+state["deaths"]

# text = "Get latest stats of covid19 on @covid.ai. Maintain social distancing and stay quarantined.\nSource : covid19india.org\n"
# caption = text + stats + "\n" + hashtag_en
# print(caption)



allhashtags = "#love #fashion #photooftheday #beautiful #art #happy #cute #picoftheday #photography #follow #tbt #followme #like4like #nature #travel #repost #style #summer #instagram #instadaily #selfie #friends #girl #fitness #fun #me #beauty #instalike #smile #family #likeforlike #life #photo #music #ootd #follow4follow #igers #amazing #makeup #nofilter #dog #model #beach #sunset #instamood #followforfollow #foodporn #motivation #l4l #sky #design #f4f #lifestyle #vscocam #cat #hair #bestoftheday #vsco #handmade #gym #dogsofinstagram #instapic #drawing #pretty #girls #flowers #artist #funny #wedding #party #instafood #photographer #inspiration #lol #cool #swag #likeforlikes #workout #fit #baby #healthy #likeforfollow #yummy #blackandwhite #christmas #foodie #moda #black #holiday #home #sea #pink #blue #london #winter #landscape #night #puppy #work #tattoo"
hashtags = random.sample(allhashtags.split(" "), 30)
print(' '.join(hashtags))