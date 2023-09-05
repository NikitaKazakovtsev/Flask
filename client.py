import requests

# response = requests.post('http://127.0.0.1:5000/notif', json={"title": 'asdasdasd',
#                                                               "description": 'sadasdasd',
#                                                               "owner": 'asdasdas'
#                                                               })
# print(response.status_code)
# print(response.text)

response = requests.get("http://127.0.0.1:5000/notif/7")
print(response.status_code)
print(response.text)


# response = requests.delete("http://127.0.0.1:5000/notif/7")
# print(response.status_code)
# print(response.text)
