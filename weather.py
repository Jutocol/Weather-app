import requests

def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For Celsius temperature, use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch weather data. Status Code: {response.status_code}")
        return None

def display_weather(data):
    if data is not None and data['cod'] == 200:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Weather data is not available.")

def main():
    api_key = "48d8507dfc18cc36ca3f25ede011cc51" 
    city = input("Enter city name: ")

    weather_data = get_weather_data(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
