# Daraz.PK Product Information API

Product Information JSON API for Daraz.PK built with 🐍 Python and 🏺 Flask and deployed using 🔼 Vercel.

## 📢 Note: This is a Free and Open Public API.
## ✔️ No authentication or keys needed!

## API Usage

This section gives you a brief introduction to the Daraz.PK API

The web API is hosted at [https://daraz-abdulalikhan.vercel.app/](https://daraz-abdulalikhan.vercel.app/)

### To query the information for a product listed on Daraz.pk 

   - 🌐 Navigate to the product's page
   - For instance:  [https://www.daraz.pk/products/ **-i220258773-s1433671472.html** ](https://www.daraz.pk/products/-i220258773-s1433671472.html)
   - Copy the portion in this link after "https://www.daraz.pk/products/"
   - Pass this portion of the product page as a parameter to the Daraz.PK API as follows:
   [https://daraz-abdulalikhan.vercel.app/-i220258773-s1433671472.html](https://daraz-abdulalikhan.vercel.app/-i220258773-s1433671472.html)

The API will respond with the following attributes for the queried product in JSON format:
- Product Name (name)
- Product Price (price)
- Seller Name (seller)
- Product Category (category)
- Product Image (image)
- Discount (discount)

### In this case, the API responds with the following JSON data

```json
{
  "category": [
    "Fashion", 
    "Men", 
    "Clothing", 
    "Casual Tops", 
    "T-Shirts"
  ], 
  "discount": "-55%", 
  "image": "https://static-01.daraz.pk/p/444c65c97cc08a4df20ac04b32b39846.jpg", 
  "name": "Select by Daraz Basic Round Neck T-Shirt For Men", 
  "price": "Rs. 550", 
  "seller": "Select by Daraz"
}
```
