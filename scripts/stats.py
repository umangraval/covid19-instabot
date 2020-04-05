from igramscraper.instagram import Instagram
from pprint import pprint
instagram = Instagram()

# authentication supported
instagram.with_credentials('covid.ai_telugu', 'CoronaCann09')
instagram.login()

# medias = instagram.get_medias("covid.ai_telugu", 5)
# # print(medias[0])
# comments = instagram.get_media_comments_by_id('2276005509759007500', 10000)
# comment = instagram.add_comment('2276005509759007500', 'nice!!')
# pprint(vars(comment))
comments = instagram.get_media_comments_by_id('2276005509759007500', 10000)

for comment in comments['comments']:
    instagram.delete_comment('2276005509759007500', comment)