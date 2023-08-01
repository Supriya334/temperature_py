import requests

def get_weather(Name_of_city, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={Name_of_city}&appid={api_key}"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        print(f"Current temperature in {Name_of_city}: {temperature_celsius:.2f}°C")
    else:
        print("Error in fetching data or invalid city name.")

def main():
    api_key = "365604482f0104c4740e4a1a416d6e40"
    
    Name_of_city = input("Enter City Name🌃🧐 ")
    
    get_weather(Name_of_city,api_key)
    print("♨️")

if __name__ == "__main__":
    main()


# print("thank you, Have a great day ahead:)")

# made by :-Supriya
# code:-cap04_146


