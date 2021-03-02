# Workout Tracking with Google Sheets
import requests

APP_ID = 'app id'
API_KEY = 'you key'

AGE = '20'
HEIGHT = '150'
WEIGHT = '75'
GENDER = 'MALE'

nutr_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "content-type": "application/json",
}
nutr_query = input("Tell me which excercises you did? ")
nutr_data= {
     "query": nutr_query,
     "gender": GENDER,
     "weight_kg": WEIGHT,
     "height_cm": HEIGHT,
     "age": AGE,
}

response = requests.post(url=nutr_endpoint, json=nutr_data, headers=headers)
result = response.json()
print(result)

