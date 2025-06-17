from django.shortcuts import render
import requests

def home(request):
    # context = {} 
    city = "No Place"
    if request.method == "POST":
        city = request.POST["q"]
        city1 = city.upper()
        key = "e689badb9eb27e62823f54dd212a0021"
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

        response = requests.get(api)
        if response.status_code == 200 :
            data = response.json()

            context = {
                'city':city1,
                "temprature": int(data['main']['temp'] - 273.15),
                "humidity": data['main']['humidity'],
                "press": data["main"]["pressure"],
                "desc": data["weather"][0]["main"],
                "icon": data["weather"][0]["icon"],
                "wind": data["wind"]["speed"],
                "see": data["sys"]["country"]

            }
        else:
            context = {
                'error': "City not found. Please enter a valid city.",
                'city': city1
            }

        return render(request,"index.html", context)
    return render(request,"index.html", {"city":city})
    