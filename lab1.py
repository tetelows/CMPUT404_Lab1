import requests

#result = requests.get("https://www.google.com")
result = requests.get("https://raw.githubusercontent.com/tetelows/CMPUT404_Lab1/main/lab1.py")
print(result.content)
#print(requests.__version__)