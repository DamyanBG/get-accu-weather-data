import requests
from decouple import config

GET_CURRENT_DATA_URL = config("ACCU_WEATHER_URL_CURRENT")
GET_PREDICTION_DATA_URL = config("ACCU_WEATHER_URL_PREDICTION")
API_KEY = config("ACCU_WEATHER_KEY")

POST_URL = "http://192.168.0.189:8000"


def get_current_data():
    r = requests.get(f"{GET_CURRENT_DATA_URL}?apikey={API_KEY}")
    resp_json = r.json()
    temperature = resp_json[0]["Temperature"]["Metric"]["Value"]
    post_body = {"temperature": temperature, "place": "Dobrich", "weather_api_pk": 2}
    p = requests.post(f"{POST_URL}/current", json=post_body)


def take_predition_data():
    r = requests.get(f"{GET_PREDICTION_DATA_URL}&apikey={API_KEY}")
    resp_json = r.json()
    print(resp_json)
    for predict in resp_json:
        temperature = predict["Temperature"]["Value"]
        prediction_for = predict["DateTime"].split("+")[0]
        post_body = {
            "place": "Dobrich",
            "temperature": temperature,
            "prediction_for": prediction_for,
            "weather_api_pk": 2,
        }
        p = requests.post(f"{POST_URL}/prediction", json=post_body)
