# Daraz.PK Product Information API

Product Information JSON API for Daraz.PK built with Python, Flask and deployed using Vercel.

## API Usage

This section gives you a brief introduction to the Daraz.PK API

The web API is hosted at [https://daraz-abdulalikhan.vercel.app/](https://daraz-abdulalikhan.vercel.app/)

To query the information for the following product: https://www.daraz.pk/products/this-is-a-test-product-i212716725-s1420886889.html
The highlighted portion represents the product's unique page.

Pass this portion of the product page as a parameter to the Daraz.PK API as follows:
https://daraz-abdulalikhan.vercel.app/this-is-a-test-product-i212716725-s1420886889.html

The API will respond with the following attributes for the queried product in JSON format:
- Product Name
- Product Price
- Seller Name
- Product Category
- Product Image
- Discount (as a Percentage)

### In this case, the API responds with the following JSON data

```json
{"category":["Pet Supplies","Dog","Dog Food","Dog Dry Food"],"discount":"","image":"https://static-01.daraz.pk/p/89cf667382e734d6522ce72eedc1eed2.jpg","name":"WOOF PUPPY FOOD 3KG","price":"Rs. 1,200","seller":"Be Happy Pets"}
{"mode":"full","isActive":false}
```
