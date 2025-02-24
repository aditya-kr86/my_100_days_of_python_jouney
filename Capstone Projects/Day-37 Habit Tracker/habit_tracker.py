import requests
from datetime import datetime

USERNAME = "PIXELA_USERNAME"
Graph_id = "GRAPH_ID"
TOKEN = "PIXELA_TOKEN"
##--------------------------------------------STEP-1----------------------------------------------##
pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token":TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
##--------------------------------------------STEP-2-Creating Graph----------------------------------------------##
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "hr.",
#     "type": "int",
#     "color": "shibafu" 
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
##--------------------------------------------STEP-3-Posting Dta----------------------------------------------##
today = datetime.now()
date = today.strftime("%Y%m%d")
# date = "20240801"
graph_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_id}"
graph_value_config = {
    "date":date,
    "quantity":input("How Many Hours You have Done Coding Today ? ")
    }
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_value_endpoint,json=graph_value_config,headers=headers)
print(response.text)
##--------------------------------------------STEP-4-PUT----------------------------------------------##
# which_date = "20240802"
# graph_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_id}/{which_date}"
# graph_value_config = {
#     "quantity":"10"
#     }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.put(url=graph_value_endpoint,json=graph_value_config,headers=headers)
# print(response.text)
##--------------------------------------------STEP-5-DELETE----------------------------------------------##
date = "20240816"
graph_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_id}/{date}"
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.delete(url=graph_value_endpoint,headers=headers)
print(response.text)
