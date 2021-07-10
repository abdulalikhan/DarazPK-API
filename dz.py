import re
import json
import requests


def fetchInfo(product):
    # Product is the part of the URL after https://www.daraz.pk/products/
    # For Example:
    # In https://www.daraz.pk/products/this-is-a-test-product-i212716725-s1420886889.html
    # product is "this-is-a-test-product-i212716725-s1420886889.html"
    url = "https://www.daraz.pk/products/" + product
    html_doc = requests.get(url).text
    data = json.loads(
        re.search(r'pdpTrackingData = ("{.*}")', html_doc).group(1))
    data = data.replace('\"', '"')
    data = json.loads(data)

    result = {}
    result['name'] = data['pdt_name']
    result['seller'] = data['seller_name']
    result['price'] = data['pdt_price']
    result['image'] = data['pdt_photo']
    result['category'] = data['pdt_category']
    result['discount'] = data['pdt_discount']
    return result
