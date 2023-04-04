from bs4 import BeautifulSoup
import requests,openpyxl
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Movie list"
sheet.append(['Rank','Movie name','Year of Release','IMDB Rating'])
try:
    response=requests.get("https://www.imdb.com/chart/top/")
    soup=BeautifulSoup(response.text,'html.parser')
    movies=soup.find('tbody',class_="lister-item-content").find_all("tr")
    for movie in movies:
        print(movie)
        
        rank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        movie_name=movie.find('td',class_="titleColumn").a.text
        rate=movie.find("td",class_="ratingColumn").strong.text
        year=movie.find("td",class_="titleColumn").span.text.replace('(',"")
        year=year.replace(')','')
        # print(rank,movie_name,year,rate)
        sheet.append([rank,movie_name,year,rate])
        
        
        
    
except Exception as e: 
    print (e)
excel.save("Movies.xlsx")
     
