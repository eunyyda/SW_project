from datetime import datetime, timedelta
import json
import pandas as pd
import requests

# 데이터 로드 (대체 데이터 사용)
import pandas as pd

# 데이터 로드 (대체 데이터 사용)
data = pd.DataFrame({
    'name': ['김해'],
    'x': [62],
    'y': [123]
})
print(data.head())


# 설정 값: 김해 좌표와 인증키
serviceKey = "1oQI%2F3dqAtfyKar463I6wrsaQ36v5gWnuVGL9oWKySPWtoVLzpVP%2BaSFpp04Kq7zje1KKPPmYoKPPRETBgTBuw%3D%3D"  # 인증키
base_date = '20241204'  # 발표 일자
base_time = '0700'  # 발표 시간
nx = '62'  # 예보 지점 x좌표
ny = '123'  # 예보 지점 y좌표

# 실제 입력 시간 계산
input_d = datetime.strptime(base_date + base_time, "%Y%m%d%H%M") - timedelta(hours=1)
input_datetime = datetime.strftime(input_d, "%Y%m%d%H%M")
input_date = input_datetime[:-4]
input_time = input_datetime[-4:]

print(f"Input Date: {input_date}, Input Time: {input_time}")

# URL 구성
url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey={serviceKey}&numOfRows=60&pageNo=1&dataType=json&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"
print(url)
params = {
    "serviceKey": serviceKey,
    "numOfRows": "60",
    "pageNo": "1",
    "dataType": "json",
    "base_date": input_date,
    "base_time": input_time,
    "nx": nx,
    "ny": ny
}

print(f"URL: {url}")
print(f"Params: {params}")

# API 호출
response = requests.get(url, params=params, verify=False)
res = json.loads(response.text)

# 응답 확인 및 데이터 처리
if response.status_code == 200:
    if 'response' in res and 'body' in res['response'] and 'items' in res['response']['body']:
        items = res['response']['body']['items']['item']
        df = pd.DataFrame(items)
        print(df.head())

        # 기온 데이터 추출
        temperature_df = df[df['category'] == 'T1H']  # 'T1H'는 기온
        temperature_df = temperature_df[['baseDate', 'baseTime', 'fcstDate', 'fcstTime', 'fcstValue']]
        temperature_df = temperature_df.rename(columns={
            'baseDate': '발표일자',
            'baseTime': '발표시간',
            'fcstDate': '예보일자',
            'fcstTime': '예보시간',
            'fcstValue': '기온'
        })
        print(temperature_df.head())
    else:
        print("No data available")
else:
    print(f"Error {response.status_code}: {response.text}")
