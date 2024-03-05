# import requests

# year = 1950
# round = 1

# url = f'http://ergast.com/api/f1/{year}/{round}/results.json'

# result = requests.get(url)

# data = result.json()


# for year in range(1950, 2024):
#     for round in range(1, 20):
#         url = f'http://ergast.com/api/f1/{year}/{round}/results.json'
#         result = requests.get(url)
#         data = result.json()
#         #print(data)
#         print(data.get("MRData").get("RaceTable")) if data.get("MRData").get("series") == "f1" else "Not F1 Data"

# #print(data)
# #print(data.get("MRData").get("RaceTable")) if data.get("MRData").get("series") == "f1" else "Not F1 Data"


import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_data(year, round):
    url = f'http://ergast.com/api/f1/{year}/{round}/results.json'
    result = requests.get(url)
    data = result.json()
    if data.get("MRData").get("series") == "f1":
        print(data.get("MRData").get("RaceTable"))
    else:
        print("Not F1 Data")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as per your requirement
        futures = []
        for year in range(1950, 2024):
            for round_num in range(1, 20):
                futures.append(executor.submit(fetch_data, year, round_num))
        
        for future in futures:
            future.result()
