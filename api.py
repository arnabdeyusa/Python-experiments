

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.amazon.com/product-reviews/B0D1BC13CL'
headers = {"User-Agent": "Mozilla/5.0"}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

reviews = []
for review in soup.find_all('div', class_='a-section review'):
    title = review.find('a', class_='review-title').find('span').text.strip()
    rating = review.find('i', class_='review-star-rating').text.strip()
    text = review.find('div', class_='review-data').text.strip()
    reviews.append([title, rating, text])

# Convert to DataFrame and export to Excel
df = pd.DataFrame(reviews, columns=['Title', 'Rating', 'Review'])
df.to_excel('amazon_reviews.xlsx', index=False)