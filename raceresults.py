import requests
import pandas as pd

def racersForYear(year):
    round = 1
    
    for race in range(1, 20):
        url = f'http://ergast.com/api/f1/{year}/{round}/results.json'
        result = requests.get(url)

        data = result.json()

        race_results = data.get("MRData").get("RaceTable").get("Races")[0].get("Results")

        drivers = []
        for race in race_results:
            driver = race.get("Driver")['driverId']
            if driver in drivers:
                continue
            drivers.append(driver)
        round+=1
    return(list(drivers))

print(racersForYear(2023))
