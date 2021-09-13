import requests
from bs4 import BeautifulSoup


url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response=requests.get(url)
html_content=response.content
rating_scala=float(input("Please enter the rating: "))
soup=BeautifulSoup(html_content,"html.parser")
movies_name=soup.find_all("td",{"class":"titleColumn"})
movies_rating=soup.find_all("td",{"class":"ratingColumn imdbRating"})

for name,rate in zip (movies_name,movies_rating):
    name=name.text
    rate=rate.text
    name=name.strip()
    name=name.replace("\n","")
    name=name.replace("      "," ")
    rate=rate.strip()
    rate=rate.replace("\n","")
    if(rating_scala<float(rate)):
        print("Movie:", name, "Rating:", rate)





