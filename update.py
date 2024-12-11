import schedule
import time
import requests

def update_weather(city):
    weather_data = get_weather_data(city)
    if weather_data:
        print(f"Updated weather for {city}: {weather_data}")
    else:
        print(f"Failed to get weather data for {city}")

def get_weather_data(city):
    # OpenWeatherMap API 설정
    api_key = "9WmYIaybS0epmCGsmytHvw" 
    base_url = "http://api.openweathermap.org/data/2.5/weather"

# API 요청
    try:
        response = requests.get(base_url, params={
            "q": city,
            "appid": api_key,
            "units": "metric"  
            # 섭씨 온도 사용
        })
        response.raise_for_status()  
        # HTTP 오류가 있는 경우 예외 발생
        
        data = response.json()
        # 필요한 정보 추출
        weather_info = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None

# lambda를 사용하여 city="Seoul"을 전달


while True:
    schedule.run_pending()
    time.sleep(1)

