# -*- coding: utf-8 -*-
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
from instabot import Bot
import schedule
import time
import glob, os
import requests, json
import shutil
import requests
from bs4 import BeautifulSoup
import json
import urllib3, random

# Trending Hashtags
allhashtags = "#love #fashion #photooftheday #beautiful #art #happy #cute #picoftheday #photography #follow #tbt #followme #like4like #nature #travel #repost #style #summer #instagram #instadaily #selfie #friends #girl #fitness #fun #me #beauty #instalike #smile #family #likeforlike #life #photo #music #ootd #follow4follow #igers #amazing #makeup #nofilter #dog #model #beach #sunset #instamood #followforfollow #foodporn #motivation #l4l #sky #design #f4f #lifestyle #vscocam #cat #hair #bestoftheday #vsco #handmade #gym #dogsofinstagram #instapic #drawing #pretty #girls #flowers #artist #funny #wedding #party #instafood #photographer #inspiration #lol #cool #swag #likeforlikes #workout #fit #baby #healthy #likeforfollow #yummy #blackandwhite #christmas #foodie #moda #black #holiday #home #sea #pink #blue #london #winter #landscape #night #puppy #work #tattoo"
hashtag_en = ' '.join(random.sample(allhashtags.split(" "), 30))
hashtag_ta = ' '.join(random.sample(allhashtags.split(" "), 30))
hashtag_te = ' '.join(random.sample(allhashtags.split(" "), 30))
hashtag_bn = ' '.join(random.sample(allhashtags.split(" "), 30))
hashtag_mn = ' '.join(random.sample(allhashtags.split(" "), 30))
hashtag_gu = ' '.join(random.sample(allhashtags.split(" "), 30))
hashtag_ka = ' '.join(random.sample(allhashtags.split(" "), 30))
hashtag_hi = ' '.join(random.sample(allhashtags.split(" "), 30))
print("en: "+hashtag_en)
print("ta: "+hashtag_ta)
print("te: "+hashtag_te)
print("bn: "+hashtag_bn)
print("mn: "+hashtag_mn)
print("ka: "+hashtag_ka)
print("hi: "+hashtag_hi)
print("gu: "+hashtag_gu)

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


# Statistics
http = urllib3.PoolManager()
r = http.request('GET', 'https://api.covid19india.org/data.json')
data =  json.loads(r.data.decode('utf-8'))
states = data["statewise"]
for state in states:
    if(state["state"] == "Total"):
        stats = "\nConfirmed: "+state["confirmed"]+"\nActive: "+state["active"]+"\nRecovered: "+state["recovered"]+"\nDeaths: "+state["deaths"]+"\n"

text = "Get latest stats of covid19 on @covid.ai. Maintain social distancing and stay quarantined.\nSource : covid19india.org\n"

bot=Bot()
langs = ['english','telugu','bengali','tamil','malayalam']
accounts = {
    'covid.ai_telugu': 'పొందండి తాజా గణాంకాలు ఆఫ్ covid19 పై @covid.ai_telugu @covid.ai. నిర్వహించడానికి సామాజిక దూరమవుతున్న మరియు బస నిర్భంధానికి. మూలం: covid19india.org\nగణాంకాలు లో భారతదేశం'+stats+hashtag_te,
    'covid.ai_bengali': 'পাওয়া সর্বশেষ পরিসংখ্যান এর covid19 চালু @covid.ai_bengali @covid.ai। বজায় রাখা সামাজিক দুরত্ব এবং থাকা আলাদা। উৎস : covid19india.org\nপরিসংখ্যান ভিতরে ভারত'+stats+hashtag_bn,
    'covid.ai_tamil': 'பெறு சமீபத்திய புள்ளிவிவரங்கள் இன் covid19 மீது @covid.ai_tamil @covid.ai. பராமரிக்கவும் சமூக இடைவெளியும் மற்றும் தங்க தனிமைப்படுத்தப்பட்ட. மூல : covid19india.org\nபுள்ளியியல் இல் இந்தியா'+stats+hashtag_ta,
    'covid.ai_malayalam': '@covid.ai_malayalam @covid.ai- ൽ covid19- ന്റെ ഏറ്റവും പുതിയ സ്ഥിതിവിവരക്കണക്കുകൾ നേടുക. സാമൂഹിക അകലം പാലിക്കുക. ഉറവിടം: covid19india.org\nഇന്ത്യയിലെ സ്ഥിതിവിവരക്കണക്കുകൾ'+stats+hashtag_mn,
    'covid.ai': 'Get latest stats of covid19 on @covid.ai. Maintain social distancing and stay quarantined.\nSource : covid19india.org\nStatistics in India'+stats+hashtag_en,
    'covid.ai_hindi': '@covid.ai @covid.ai_hindi पर covid19 के नवीनतम आँकड़े प्राप्त करें। सामाजिक दूरी बनाए रखें और संगरोध रहें। \nस्रोत: covid19india.org\n'+stats+hashtag_hi,
    'covid.ai_gujarati': '@covid.ai @covid.ai_gujarati પર નવીનતમ આંકડા મેળવો. સામાજિક અંતર જાળવવા અને અલગ રહેવું.\nસ્રોત: covid19india.org\nભારતમાં આંકડા'+stats+hashtag_gu,
    'covid.ai_kannada': '@covid.ai @covid.ai_kannada ನಲ್ಲಿ  covid19 ನ ಇತ್ತೀಚಿನ ಅಂಕಿಅಂಶಗಳನ್ನು ಪಡೆಯಿರಿ. ಸಾಮಾಜಿಕ ದೂರವನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಿ ಮತ್ತು ಪ್ರತ್ಯೇಕವಾಗಿರಿ.\nಮೂಲ: covid19india.org\nಭಾರತದಲ್ಲಿ ಅಂಕಿಅಂಶಗಳು'+stats+hashtag_ka
    }

def upload_photo(username):
    bot.login(username=username,password="CoronaCann09")
    listofimgs = glob.glob("./Posts/*")
    img_path = listofimgs[0]
    bot.upload_photo(img_path,caption=accounts[username])
    to_remove_path = img_path+".REMOVE_ME"
    os.remove(to_remove_path)
    bot.logout(username=username,password="CoronaCann09")

# Task scheduling
os.system("python map_generator.py")
upload_photo("covid.ai_gujarati")
time.sleep(5)
upload_photo("covid.ai_hindi")
time.sleep(5)
upload_photo("covid.ai_kannada")
time.sleep(5)
upload_photo("covid.ai")
time.sleep(5)
#upload_photo("covid.ai_malayalam")
time.sleep(5)
#upload_photo("covid.ai_bengali")
time.sleep(5)
upload_photo("covid.ai_telugu")
time.sleep(5)
upload_photo("covid.ai_tamil")
shutil.rmtree('config')
