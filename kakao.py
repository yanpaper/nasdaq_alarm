#https://developers.kakao.com/console/app/758868
#https://developers.kakao.com/tool/rest-api/open/post/v2-api-talk-memo-default-send
#https://gam860720.tistory.com/522
#https://gam860720.tistory.com/523
#https://velog.io/@hibeen1/Python%EC%9C%BC%EB%A1%9C-%EB%82%98%EC%97%90%EA%B2%8C-%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%86%A1-%EB%B3%B4%EB%82%B4%EA%B8%B0

#https://yobbicorgi.tistory.com/36




import requests
import json
import time

#code url https://kauth.kakao.com/oauth/authorize?client_id=b328b5caff640883672534d3fd6f277a&redirect_uri=https://example.com/oauth&response_type=code
url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'b328b5caff640883672534d3fd6f277a'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'PHAwYvLvcYEV0sp_PEbEt2FUT1sD435vB52M_m6zocj2UisTDyJn99DMgCtOIyDP6PJCAQopb7gAAAGBcfHd-w'


def f_auth():
    data = {
        'grant_type': 'authorization_code',
        'client_id': rest_api_key,
        'redirect_uri': redirect_uri,
        'code': authorize_code,
    }

    response = requests.post(url, data=data)
    tokens = response.json()

    with open("token.json", "w") as fp:
        json.dump(tokens, fp)
    with open("token.json", "r") as fp:
        ts = json.load(fp)
    r_token = ts["refresh_token"]
    return r_token


def f_auth_refresh(r_token):
    with open("token.json", "r") as fp:
        ts = json.load(fp)
    data = {
        "grant_type": "refresh_token",
        "client_id": rest_api_key,
        "refresh_token": r_token
    }
    response = requests.post(url, data=data)
    tokens = response.json()

    with open(r"token.json", "w") as fp:
        json.dump(tokens, fp)
    with open("token.json", "r") as fp:
        ts = json.load(fp)
    token = ts["access_token"]
    return token


def f_send_talk(token, text):
    header = {'Authorization': 'Bearer ' + token}
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    post = {
        'object_type': 'text',
        'text': text,
        'link': {
            'web_url': 'https://developers.kakao.com',
            'mobile_web_url': 'https://developers.kakao.com'
        },
        'button_title': '키워드'
    }
    data = {'template_object': json.dumps(post)}
    return requests.post(url, headers=header, data=data)


r_token = f_auth()


while True:
    token = f_auth_refresh(r_token)
    f_send_talk (token, '보낼 메시지')
    time.sleep(1800)