import requests

# Making a GET request
response = requests.get("https://api.github.com")

# Checking if the request was successful
if response.status_code == 200:
    # Parsing JSON data
    data = response.json()
    print(data)
else:
    print(f"Failed to fetch data: {response.status_code}")

# Making a POST request with form data
payload = {"key1": "value1", "key2": "value2"}
response = requests.post("https://httpbin.org/post", data=payload)

# Printing the response text
print(response.text)
