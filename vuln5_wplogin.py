import requests

# URL to send the POST request
url = "https://www.teknofestpakistan.com/wp-login.php"

# Payload with login credentials and other form data
payload = {
    'log': 'afsdf',  # Username
    'pwd': 'afsdfsd',  # Password
    'wp-submit': 'Log In',
    'redirect_to': 'https://www.teknofestpakistan.com/wp-admin/admin.php',
    'testcookie': '1'
}

# Headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,ur;q=0.8',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.teknofestpakistan.com',
    'Referer': 'https://www.teknofestpakistan.com/wp-login.php',
    'Upgrade-Insecure-Requests': '1'
}

# Send the POST request
response = requests.post(url, data=payload, headers=headers)

# Print the response from the server
print(response.text)
