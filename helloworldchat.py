#--coding:utf8;--
#qpy:quiet
"""
This is an example file which tell you how to use QPython to develop android app.
It use the SL4A feature and the quiet feature which run background

@Author: River
@Date: 2012-12-31
"""
#import androidhelper
import urllib.parse
import urllib.request
##droid.ttsSpeak('कैसे हो आप')
#txt=droid.recognizeSpeech()
#droid.ttsSpeak(txt.result)
txt='Hello'
url = 'http://mobihangama-chat.herokuapp.com/prediction'
values ="{\"message\" :\""+ txt +"\" }"
headers = {}
headers['Content-Type'] = 'application/json'

data = values.encode("utf-8")# data should be bytes
req = urllib.request.Request(url, data=data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   print(the_page)
