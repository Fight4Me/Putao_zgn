#encoding=utf8
"""
Created on Tue Nov 20 12:11:27 2018

@author: bnuzgn
"""
import json
import http.client



def post_standard(standardData):
    url = standardData['url']
    text = standardData['text']
    audio = standardData['voice']
    appkey = {'appkey': 'wlghphduewl2onovahuvyhj4jyfsjztk3dm7bpa4'}
    
    connection = http.client.HTTPSConnection('http://cm.edu.hivoice.cn:20010')
    connection.request('POST','/mp3',data ={'text': text} ,files={'voice':('upload.mp3', open(audio, 'rb'))},headers=appkey)
    ret = connection.getresponse()
#    data = {'text':text}
#    ret = req.post(url, data ={'text': text} ,files={'voice':('upload.mp3', open(audio, 'rb'))},headers=appkey).content
#    print (url,text,audio)
    return ret

def post_user():
    return ret

def get_syllable(data):
    refer = data['refer_syllable']
    ans = data['answer']
    syllable = data['syllable']

    url = 'http://edu.hivoice.cn:8085/eval/mp3' 

    sc = data['sc']
    mode = data['mode']


    h = {'appkey': 'wlghphduewl2onovahuvyhj4jyfsjztk3dm7bpa4',
        'score-coefficient': str(sc)}
    syllable = syllable.split('|')

    text={"Version":1,"DisplayText":ans,"Markers":[{"Type":"phone","Position":{"Start":0,"Length":len(ans)},"Value":[u"·".join(syllable).encode('utf8')]}]}


    c = req.post(url, 
            data={'text': json.dumps(text), 'mode': mode},
            files={'voice':('upload.mp3', open(refer, 'rb'))},
            headers=h).content

    return c

if __name__ == '__main__':
#    data = {}
#    data['refer_syllable'] = r'C:\Users\bnuzgn\Desktop\putao\11_26\4.mp3'
#    data['answer'] = 'v'
#    data['syllable'] = u"v" 
#    data['sc'] = 1.0
#    data['mode'] = 'D'
#    print (get_syllable(data))
    standardData = {}
    standardData['text'] = 'jump rope'
    standardData['voice'] = r'C:\Users\bnuzgn\Desktop\putao\11_26\4.mp3'
    standardData['url'] = 'http://cm.edu.hivoice.cn:20010/mp3'
    print (post_standard(standardData))