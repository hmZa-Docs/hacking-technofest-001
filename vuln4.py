import requests

url = "https://www.teknofestpakistan.com/wp-admin/admin-ajax.php"

# Payload data
payload = {
    "action": "elementor_menu_cart_fragments",
    "templates[]": "7",
    "templates[]": "1812",
    "templates[]": "1819",
    "_nonce": "069329e585",
    "is_editor": "false"
}

# Headers
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,ur;q=0.8",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.teknofestpakistan.com",
    "referer": "https://www.teknofestpakistan.com/cart/",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

# Cookies
cookies = {
    "_lscache_vary": "0d7874c30385bb288fd74ae9b413fd0c",
    "sbjs_migrations": "1418474375998%3D1",
    "sbjs_current_add": "fd%3D2024-10-07%2013%3A42%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.teknofestpakistan.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F",
    "sbjs_first_add": "fd%3D2024-10-07%2013%3A42%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.teknofestpakistan.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F",
    "sbjs_current": "typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29",
    "sbjs_first": "typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29",
    "sbjs_udata": "vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36",
    "_fbp": "fb.1.1728308576176.779551137770418641",
    "woocommerce_items_in_cart": "1",
    "woocommerce_cart_hash": "495641226e1a4db64584f35fdae1be43",
    "wp_woocommerce_session_8d30e5abd0f2077eb16c103f50b5c9ac": "t_c7f2c882706cfa73f7cb2309f40575%7C%7C1728481622%7C%7C1728478022%7C%7C6c18186453ffd1cfc732f91253c6f98a",
    "sbjs_session": "pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.teknofestpakistan.com%2Fcart%2F"
}

# Send the POST request
response = requests.post(url, data=payload, headers=headers, cookies=cookies)

# Print the response status code and content
print("Status Code:", response.status_code)
print("Response Body:", response.text)
