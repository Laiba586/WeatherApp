from django.shortcuts import render
import requests

def weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        apikey = '8ed71e95a521fc3afaa1f61910da398b'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric'
        
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            context = {
                'weather': {
                    'name': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
            }
        else:
            context = {'error': 'City not found or API error'}

        return render(request, 'myweather/weather.html', context)

    return render(request, 'myweather/weather.html')
