import requests
import datetime as dt
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv("REACT_APP_TOKEN")
USERNAME = os.getenv("REACT_APP_USERNAME")

# https: // pixe.la / @ bee8498

user_config = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

header = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph1",
    "name": "coding",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}

# today = dt.datetime.now()
# print(today)

yesterday = dt.datetime(year=2022, month=8, day=7)
# print(yesterday.strftime("%Y%m%d"))

pixel_config = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "10",
}

# # Step:: 1
# response = requests.post(url="https://pixe.la/v1/users", json=user_config)
# print(response.text)

# # Step:: 2
# response = requests.post(url="https://pixe.la/v1/users/bee8498/graphs", json=graph_config, headers=header)
# print(response.text)

# # Step:: 3
# response = requests.post(url="https://pixe.la/v1/users/bee8498/graphs/graph1", json=pixel_config, headers=header)
# print(response.text)

update_config = {
    "quantity": "7"
}

# Step:: 4 -> update
# response = requests.put(url=f"https://pixe.la/v1/users/bee8498/graphs/graph1/{yesterday.strftime('%Y%m%d')}",
#                         json=update_config, headers=header)
# print(response.text)

GRAPH_ID = "graph1"

# Step:: 5 -> delete
response = requests.delete(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}",
                           headers=header)
print(response.text)
