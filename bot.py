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

URL_indian = "http://best-hashtags.com/hashtag/indian/"
URL_corona = "http://best-hashtags.com/hashtag/coronavirus/"

r_indian = requests.get(URL_indian) 
r_corona = requests.get(URL_corona) 

soup_indian = BeautifulSoup(r_indian.content, 'html.parser') 
soup_corona = BeautifulSoup(r_corona.content, 'html.parser') 

hashtag_indian = ' '.join(soup_indian.find('p1').getText().split(" ")[1:21])
hashtag_corona = ' '.join(soup_corona.find('p1').getText().split(" ")[1:11])
hashtags = hashtag_indian +' '+ hashtag_corona

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
    'covid.ai_telugu': 'పొందండి తాజా గణాంకాలు ఆఫ్ covid19 పై @covid.ai_telugu @covid.ai. నిర్వహించడానికి సామాజిక దూరమవుతున్న మరియు బస నిర్భంధానికి. మూలం: covid19india.org\nగణాంకాలు లో భారతదేశం'+stats+hashtags,
    'covid.ai_bengali': 'পাওয়া সর্বশেষ পরিসংখ্যান এর covid19 চালু @covid.ai_bengali @covid.ai। বজায় রাখা সামাজিক দুরত্ব এবং থাকা আলাদা। উৎস : covid19india.org\nপরিসংখ্যান ভিতরে ভারত'+stats+hashtags,
    'covid.ai_tamil': 'பெறு சமீபத்திய புள்ளிவிவரங்கள் இன் covid19 மீது @covid.ai_tamil @covid.ai. பராமரிக்கவும் சமூக இடைவெளியும் மற்றும் தங்க தனிமைப்படுத்தப்பட்ட. மூல : covid19india.org\nபுள்ளியியல் இல் இந்தியா'+stats+hashtags,
    'covid.ai_malayalam': '@covid.ai_malayalam @covid.ai- ൽ covid19- ന്റെ ഏറ്റവും പുതിയ സ്ഥിതിവിവരക്കണക്കുകൾ നേടുക. സാമൂഹിക അകലം പാലിക്കുക. ഉറവിടം: covid19india.org\nഇന്ത്യയിലെ സ്ഥിതിവിവരക്കണക്കുകൾ'+stats+hashtags,
    'covid.ai': 'Get latest stats of covid19 on @covid.ai. Maintain social distancing and stay quarantined.\nSource : covid19india.org\nStatistics in India'+stats+hashtags,
    'covid.ai_hindi': '@covid.ai @covid.ai_hindi पर covid19 के नवीनतम आँकड़े प्राप्त करें। सामाजिक दूरी बनाए रखें और संगरोध रहें। \nस्रोत: covid19india.org\n'+stats+hashtags,
    'covid.ai_gujarati': '@covid.ai @covid.ai_gujarati પર નવીનતમ આંકડા મેળવો. સામાજિક અંતર જાળવવા અને અલગ રહેવું.\nસ્રોત: covid19india.org\nભારતમાં આંકડા'+stats+hashtags,
    'covid.ai_kannada': '@covid.ai @covid.ai_kannada ನಲ್ಲಿ  covid19 ನ ಇತ್ತೀಚಿನ ಅಂಕಿಅಂಶಗಳನ್ನು ಪಡೆಯಿರಿ. ಸಾಮಾಜಿಕ ದೂರವನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಿ ಮತ್ತು ಪ್ರತ್ಯೇಕವಾಗಿರಿ.\nಮೂಲ: covid19india.org\nಭಾರತದಲ್ಲಿ ಅಂಕಿಅಂಶಗಳು'+stats+hashtags,
    'covid.ai_marathi': '@covid.ai @covid.ai_marathi वर कोविड 19 ची नवीनतम आकडेवारी मिळवा. सामाजिक अंतर राखणे आणि अलग ठेवणे.\nस्त्रोत: covid19india.org\nभारतातील आकडेवारी'+stats+hashtags
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
upload_photo("covid.ai_malayalam")
time.sleep(5)
upload_photo("covid.ai_bengali")
time.sleep(5)
upload_photo("covid.ai_marathi")
time.sleep(5)
#upload_photo("covid.ai_telugu")
#time.sleep(5)
upload_photo("covid.ai_tamil")
shutil.rmtree('config')
