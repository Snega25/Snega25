from bs4 import BeautifulSoup
import requests,openpyxl
# excel=openpyxl.Workbook()
# sheet=excel.active
# sheet.title="Movie list"
# sheet.append(['Rank','Movie name','Year of Release','IMDB Rating'])
try:
    response=requests.get("https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=EYNHRRHFJ637MM3F5A42&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2")
    soup=BeautifulSoup(response.text,'html.parser')
    print(soup)
        # rank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        # movie_name=movie.find('td',class_="titleColumn").a.text
        # rate=movie.find("td",class_="ratingColumn").strong.text
        # year=movie.find("td",class_="titleColumn").span.text.replace('(',"")
        # year=year.replace(')','')
        # print(rank,movie_name,year,rate)
        # sheet.append([rank,movie_name,year,rate])
    
except Exception as e: 
    print (e)
# excel.save("Movies.xlsx")       