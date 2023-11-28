import requests

# CREATE a product -> POST
new_product = {"id": 100, "title": "notebook", "price": 19.99}
response = requests.post("https://dummyjson.com/products/add", data=new_product)
print(response.text, "status code:", response.status_code)

# READ a product -> GET
product_id = 100
response = requests.get(f"https://dummyjson.com/products/{product_id}")
if response.status_code == 200:
    product = response.text
    print(product)
else:
    print("Something wrong happened: ", response.status_code)

# READ all products -> GET | [Optional] limit the request to 10 products
response = requests.get("https://dummyjson.com/products", params={"limit": 10})
response_json = response.json()
product_list = response_json["products"]
for p in product_list:
    print(p["title"])

# UPDATE a product -> PUT / PATCH
product_for_put = {"id": 100, "title": "notebook", "price": 17.99}
response = requests.put(f"https://dummyjson.com/products/{product_for_put['id']}", data=product_for_put)
print(response.text)

product_for_patch = {"price": 15.99}
response = requests.patch("https://dummyjson.com/products/100", data=product_for_patch)
print(response.text)

# DELETE a product -> DELETE
response = requests.delete("https://dummyjson.com/products/100")
print(response.text)
print(response.status_code)

# How to authenticate using username and password
username_and_password = {"username": "kminchelle", "password": "0lelplR"}
response = requests.post("https://dummyjson.com/auth/login", data=username_and_password)
token = response.json()["token"]
print(token)

# GET with token authorization
headers = {"Authorization": f"Bearer {token}"}
response = requests.get("https://dummyjson.com/auth/products/1", headers=headers)
print(response.text, "status code:", response.status_code)
