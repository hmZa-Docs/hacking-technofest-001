import json
from colorama import Fore, Style

# Sample data to simulate the request and cookies
request_data_with_cookies = {
    "Request URL": "https://www.teknofestpakistan.com/?s=<script>alert(\"hello\")</script>",
    "Request Method": "GET",
    "Status Code": "200 OK",
    "Remote Address": "93.127.173.199:443",
    "Cookies": {
        "_fbp": "fb.1.1728308576176.779551137770418641",
        "_lscache_vary": "0d7874c30385bb288fd74ae9b413fd0c",
        "sbjs_current": "typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic",
        # Add other cookies as needed
    }
}

request_data_without_cookies = {
    "Request URL": "https://www.teknofestpakistan.com/?s=<script>alert(\"hello\")</script>",
    "Request Method": "GET",
    "Status Code": "200 OK",
    "Remote Address": "93.127.173.199:443",
    "Cookies": {}
}

def display_request_info(request_data):
    print(Fore.CYAN + "== Request Information ==" + Style.RESET_ALL)
    for key, value in request_data.items():
        if isinstance(value, dict):  # Check if value is cookies
            print(Fore.YELLOW + f"{key}:" + Style.RESET_ALL)
            for cookie_key, cookie_value in value.items():
                print(Fore.GREEN + f"  - {cookie_key}: {cookie_value}" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTMAGENTA_EX + f"{key}: {value}" + Style.RESET_ALL)
    print(Fore.CYAN + "========================" + Style.RESET_ALL)

# Display request with cookies
print(Fore.BLUE + "\n=== Request with Cookies ===" + Style.RESET_ALL)
display_request_info(request_data_with_cookies)

# Display request without cookies
print(Fore.BLUE + "\n=== Request without Cookies ===" + Style.RESET_ALL)
display_request_info(request_data_without_cookies)
