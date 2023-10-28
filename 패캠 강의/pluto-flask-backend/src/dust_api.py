import requests # poetry add requests -> 서버에 요청을 보낼 수 있도록 도와주는 library
import json

def get_dust_data():

    endpoint_url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc"
    service_path = "/getMsrstnAcctoRltmMesureDnsty" # 미세먼지

    API_KEY = 'Cgs0GXYhzr575Qe/rX4aDesVhT0Ge/wzoHN46fTDGyru2lODZ1DA1tOgPuGZ1RvQ64qLQ+y6MeOnYrv7EHctzA=='
    # STATION_NAME = input('궁금한 지역을 입력하세요 : ')
    
    params = {
        'serviceKey' : API_KEY,
        'returnType' : 'json',
        'numOfRows' : 1,
        'pageNo' : 1,
        'stationName' : '강남구',
        'dataTerm' : 'DAILY',
        'ver' : '1.0'
    }

    res = requests.get(f"{endpoint_url}{service_path}", params=params)

    if res.status_code == 200:
        print("Data get success")
        data = json.loads(res.text)
        print("data", data)
    else:
        print("Request failed error: {}".format(res.status_code))

get_dust_data()