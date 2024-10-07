import requests

# Define the URL for the cart update, or any endpoint that requires a POST request
url = "https://www.teknofestpakistan.com/update_cart"

# Simulate a POST request without a CSRF token
data = {
    'cart_item': 'item_id_123',
    'quantity': 1,
    # Missing CSRF token or altered token here
    'security': 'fake_csrf_token'
}

# Send the POST request
response = requests.post(url, data=data)

# Check the response
if response.status_code == 200:
    print("CSRF test passed: Vulnerability exists. Request succeeded without a valid token.")
else:
    print("CSRF test failed: Server properly rejected the request.")
    print(f"RESPONCE:\n===============\n{response}")
