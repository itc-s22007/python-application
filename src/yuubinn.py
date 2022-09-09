import json

import requests

while True:

    s = input("郵便番号")

    url = "https://zipcloud.ibsnet.co.jp/api/search"
    param = {"zipcode": s}
    data = requests.get(url, param).json()
    address = data["results"][0]
    print(address["address1"], address["address2"], address["address3"])
    if res := input("入力を続けますか？ y or n") != "y":
        break
