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


workout_date = datetime.now().strftime("%d/%m/%Y")
workout_time = datetime.now().strftime("%X")

sheety_endpoint = 'https://api.sheety.co/0b5ce03c8fff1b3df4cc1a751a285277/workoutsTracking/workouts'


for exercise in result['exercises']:
    sheety_data = {
        'workout': {
            "date": workout_date,
            "time": workout_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }


sheety_response = requests.post(url=sheety_endpoint, json=sheety_data)
# sheety_response = requests.get(sheety_endpoint)
print(sheety_response.text)