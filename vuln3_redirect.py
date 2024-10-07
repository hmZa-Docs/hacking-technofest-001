import requests

# The URL where the redirect happens
url = "https://www.teknofestpakistan.com/redirect"

# Malicious URL for testing open redirect
params = {
    'url': 'https://yuri-is-on-rage-mode.github.io/'
}

# Send the GET request with the malicious URL
response = requests.get(url, params=params, allow_redirects=False)

# Check the response headers to see if the redirect happened
if 'Location' in response.headers and 'https://yuri-is-on-rage-mode.github.io/' in response.headers['Location']:
    print("Open Redirect test passed: Vulnerability exists. Redirected to malicious website.")
else:
    print("Open Redirect test failed: Redirect to untrusted site not allowed.")
