import pandas as pd
import io
from PIL import Image, ImageDraw, ImageFont
import json
import urllib3
import os

if __name__ == "__main__":

    print('Fetching Data...')
    print('India Data')
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://api.covid19india.org/data.json')
    data =  json.loads(r.data.decode('utf-8'))
    newdata = {
        "success": "true",
        "data":{
            "summary":{},
            "regional":[]
        }
    }
    states = data["statewise"]
    for state in states:
        if(state["state"] == "Total"):
            tt = {}
            tt["total"] = state["confirmed"]
            tt["discharged"] = state["recovered"]
            tt["deaths"] = state["deaths"]
            newdata["data"]["summary"] = tt
        else:
            st = {}
            st["loc"] = state["state"]
            st["confirmedCases"] = state["confirmed"]
            st["discharged"] = state["recovered"]
            st["deaths"] = state["deaths"]
            newdata["data"]["regional"].append(st)

    # Getting the Summary Stats
    total = int(newdata['data']['summary']['total'])
    recovered = int(newdata['data']['summary']['discharged'])
    death = int(newdata['data']['summary']['deaths'])
    active = int(total - (recovered + death))

    summ = [total, active, recovered, death]
    ## World Data
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://coronavirus-19-api.herokuapp.com/all')
    data =  json.loads(r.data.decode('utf-8'))
    w_t = data['cases']
    w_d = data['deaths']
    w_r = data['recovered']
    w_a = w_t - (w_r + w_d)

    w = [w_t,w_a,w_r,w_d]



    new = pd.DataFrame.from_dict(newdata['data']['regional'])
    print('Data Fetched')


    print('Reading Points File....')
    points_file = pd.read_csv('via_export_csv.csv')
    states = list(points_file.region_id)


    cx = []
    cy = []
    print('Generating the Image....')
    for i in range(len(states)):
        cx.append(json.loads(points_file.region_shape_attributes[i])['cx'])
        cy.append(json.loads(points_file.region_shape_attributes[i])['cy'])

    os.replace("./NEW 2.png", "./Posts/NEW 2.png")
    back = Image.open('./Posts/NEW 2.png')
    draw = ImageDraw.Draw(back)
    font = ImageFont.truetype("Fonts/Rajdhani-Bold.ttf", 27)
    for i,st in enumerate(states[:-4]):
        count = new.loc[new['loc'] == st]['confirmedCases'].values
        count = int(count[0])
        if count !=0:
            draw.text((cx[i], cy[i]), str(count), font=font, fill = 'blue')

    font = ImageFont.truetype("Fonts/Rajdhani-Bold.ttf", 30)

    j = 0
    for i in range(37,41):
        # National Stat
        draw.text((cx[i]+5, cy[i]), str(summ[j]), font=font, fill = 'red')
        # World Stat
        draw.text((cx[i]+115, cy[i]), str(w[j]), font=font, fill = 'red')
        j+=1

    lang = ['english', 'tamil', 'telugu', 'bengali', 'malayalam']
    for lan in lang:
        back = back.convert("RGB")
        back.save('./Posts/'+lan+'.jpg')
    os.replace("./Posts/NEW 2.png", "./NEW 2.png")

    print('Image Generated')
