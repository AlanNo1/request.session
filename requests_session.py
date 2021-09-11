#coding:utf-8
import requests
import re

def login():
    # url
    url = 'https://github.com/login'
    url2 ='https://github.com/session'
    url3 = 'https://github.com/explore'

    # session
    session = requests.session()

    # headers
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    # 登录
    res1 = session.get(url,headers=session.headers).content.decode()
    authenticity_token = re.findall('name="authenticity_token" value="(.*?)" /> ',res1)[0]
    print(authenticity_token)
    timestamp_secret = re.findall('name="timestamp_secret" value="(.*?)" ',res1)[0]
    print(timestamp_secret)
    timestamp = re.findall('name="timestamp" value="(.*?)"',res1)[0]
    print(timestamp)
    required_field=re.findall('<input type="text" name="(.*?)"',res1)[0]
    print(required_field)

    # formdata
    formdata = {
        'commit': 'Sign+in',
        'authenticity_token': authenticity_token,
        'login': '1924885288%40qq.com',
        'password': 'fls%40132302007',
        'trusted_device': '',
        'webauthn-support': 'supported',
        'webauthn-iuvpaa-support': 'supported',
        'return_to':'https%3A%2F%2Fgithub.com%2Flogin',
        'allow_signup':'' ,
        'client_id':'' ,
        'integration': '',
        required_field:'' ,
        'timestamp': timestamp,
        'timestamp_secret': timestamp_secret,
    }


    # 验证登录
    response1 = session.post(url2,data=formdata)
    response2 = session.get(url3)
    with open('github_with_session.html', 'wb') as f:
        f.write(response2.content)

login()