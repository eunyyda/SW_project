import requests
import json
from django.shortcuts import render
from datetime import datetime, timedelta



def home(request):

    serviceKey = "6MuNyJ2iZ6UtRMkJYOisiukvm7IFJJa%2BGVgtB32iEh%2Fb4R1dc0nq7u2yOFiDVs6fr4wWuF2sIW%2BCyKAgX1B8iA%3D%3D"
    base_date = datetime.now().strftime("%Y%m%d")  # 오늘 날짜
    base_time = "0700"  # API 기준 시간 (보통 매 시각 발표)
    nx = "62"  # 김해 x 좌표
    ny = "123"  # 김해 y 좌표

    # 실제 입력 시간 계산
    input_d = datetime.strptime(base_date + base_time, "%Y%m%d%H%M") - timedelta(hours=1)
    input_datetime = datetime.strftime(input_d, "%Y%m%d%H%M")
    input_date = input_datetime[:-4]
    input_time = input_datetime[-4:]

    # URL 구성
    url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"
    params = {
        "serviceKey": serviceKey,
        "numOfRows": "60",
        "pageNo": "1",
        "dataType": "json",
        "base_date": input_date,
        "base_time": input_time,
        "nx": nx,
        "ny": ny,
    }
    response = requests.get(url)

    # 응답 텍스트를 JSON으로 파싱
    res = json.loads(response.text)


    # 원하는 데이터 추출 (예: 기온, 날씨 상태, 강수 여부)
    forecast_items = res['response']['body']['items']['item']
    weather_data = {
        'temperature': None,
        'sky': None,
        'rain': None
    }

    for item in forecast_items:
        if item['category'] == 'T1H':  # 기온
            weather_data['temperature'] = item['fcstValue']
        elif item['category'] == 'SKY':  # 날씨 상태
            weather_data['sky'] = item['fcstValue']
        elif item['category'] == 'RN1':  # 강수 여부
            weather_data['rain'] = item['fcstValue']

    context = {
        'weather_data': weather_data
    }

    return render(request, 'home.html', context)





