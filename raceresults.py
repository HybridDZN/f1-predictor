import requests
import pandas as pd

year = 2000
round = 1

url = f'http://ergast.com/api/f1/{year}/{round}/results.json'

result = requests.get(url)

data = result.json()

race_results = data.get("MRData").get("RaceTable").get("Races")[0].get("Results")

df = pd.DataFrame(race_results)

df.to_csv('data.csv', index=False)
