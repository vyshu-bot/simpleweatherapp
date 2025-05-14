from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "8b3042c30f024d0284172752250705"  # Your WeatherAPI key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        return weather(city)
    return render_template('index.html')

@app.route('/weather/<city>')
def weather(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=7"
    res = requests.get(url)
    data = res.json()

    # Current Weather
    weather_data = {
        'city': data['location']['name'],
        'temp': data['current']['temp_c'],
        'condition': data['current']['condition']['text'],
        'humidity': data['current']['humidity'],
        'wind': data['current']['wind_kph']
    }

    # Forecast
    forecast_data = data['forecast']['forecastday']

    return render_template('weather.html', weather=weather_data, forecast=forecast_data)

if __name__ == '__main__':
    app.run(debug=True)
