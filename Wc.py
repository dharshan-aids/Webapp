from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            full_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
            response = requests.get(full_url)
            if response.status_code == 200:
                data = response.json()
                weather = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                weather = {'error': 'City not found!'}
    return render_template('index.html', weather=weather)
