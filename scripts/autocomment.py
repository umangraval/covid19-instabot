from igramscraper.instagram import Instagram
from firebase import firebase
instagram = Instagram()
firebase = firebase.FirebaseApplication('https://covidai-1dd78.firebaseio.com/', None)
data = firebase.get('/covidai-1dd78/latest_media/-M3f_ZqzLKNGLoqFP5Mr/-M3gWKCfYoXQpB0gbGJh', '')
media_ids = data['medias']
# authentication supported
instagram.with_credentials('covid.ai_bengali', 'CoronaCann09')
instagram.login()
# datas = firebase.post('/covidai-1dd78/latest_media/-M3f_ZqzLKNGLoqFP5Mr/-M3gWKCfYoXQpB0gbGJh', da)
media = instagram.get_current_top_medias_by_tag_name('corona')
print(media)
for m in media:
    if m.identifier not in media_ids:
        media_ids.append(m.identifier)
        comment = instagram.add_comment(m.identifier, 'Follow @covid.ai for the latest coronavirus stats')
        print(comment)
result = firebase.put('/covidai-1dd78/latest_media/-M3f_ZqzLKNGLoqFP5Mr/-M3gWKCfYoXQpB0gbGJh', 'medias', media_ids)
print(result)
        