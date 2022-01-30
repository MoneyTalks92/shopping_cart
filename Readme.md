# how to use this project

1. clone the repo, cd into th repo, then create virtualenv:

```
git clone repo...
cd repo
virtualenv -p python3 venv
```

2. activate the virtualenv:

on mac:

`source venv/bin/activate`

on windows: 

`venv\Scripts\activate`

3. install the dependencies:

`pip install -r requirements.txt`

4. run the app:

`python manage.py runserver`


REST API

POST Request

http://127.0.0.1:8000/cart-items/

Response

"message": "New item has been added to the Cart with id: 1"

GET Request

http://127.0.0.1:8000/cart-items/

Response


"items": 

        "product_name": 
        "product_price": 
        "product_quantity": 



PATCH Request

http://127.0.0.1:8000/update-item/1

Response

"message": "Item 1 has been updated"

DELETE Request

http://127.0.0.1:8000/delete-item/1

Response

"message": "Item 1 has been deleted"