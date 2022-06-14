from requests import Request, Session, Response
import os

def weather(lat, lon, api_key):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        parameters = {
            'lat': lat,
            'lon': lon,
            'appid': api_key
        }
        session = Session()
        request = Request('GET', url, params=parameters)
        prepped = request.prepare()
        response = session.send(prepped)
        return response.json()
    
    except Exception as e:
        return e


lat = os.environ['LAT']
lon = os.environ['LON']
api_key = os.environ['API_KEY']

print(weather(lat,lon,api_key))