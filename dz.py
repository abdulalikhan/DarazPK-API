from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')


def fetchInfo(product):
    # Product is the part of the URL after https://www.daraz.pk/products/
    # For Example:
    # In https://www.daraz.pk/products/this-is-a-test-product-i212716725-s1420886889.html
    # product is "this-is-a-test-product-i212716725-s1420886889.html"
    url = "https://www.daraz.pk/products/" + product
    driver = webdriver.Chrome('chromedriver', options=chrome_options)
    driver.get(url)
    try:
        name = driver.find_element_by_xpath(
            '//*[@id="module_product_title_1"]/div/div/span')
        price = driver.find_element_by_xpath(
            '//*[@id="module_product_price_1"]/div/div/span')
        product_detail = driver.find_element_by_xpath(
            '//*[@id="module_product_detail"]/div')
        rating = driver.find_element_by_xpath(
            '//*[@id="module_product_review"]/div/div[1]/div[2]/div/div/div[1]/div[1]/span[1]')
        seller = driver.find_element_by_xpath(
            '//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a[1]')
        data = {}
        data['name'] = name.text
        data['price'] = price.text
        data['seller'] = seller.text
        data['product_detail'] = product_detail.text
        data['rating'] = rating.text
        data['url'] = url
        driver.quit()
        return data
    except NoSuchElementException as e:
        driver.quit()
        return {"status": False, "error": "Failed to retrieve product information"}
