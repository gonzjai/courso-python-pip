import requests

def get_categories():
    r = requests.get('http://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    for elements in categories:
        print(elements['name'])