# scraping a website and storing the information acquired in a CVS file or Excel
# https://www.youtube.com/watch?v=ng2o98k983k&t=1370s
#=============important Links==========================================#
#https://github.com/Kristian-Roopnarine/Digital-Market-Place
#https://github.com/drewblay/Personal-Finance-Django-App
#https://github.com/TusharKapoor23/django-expense-tracker
#=======================================================================
#===============================tutorial Links=========================
#https://dev.to/amartyadev/flutter-app-authentication-with-django-backend-1-21cp
#https://morioh.com/p/6ca2176eccbf
#https://www3.unifr.ch/inf/softeng/en/assets/public/files/research/students_projects/bachelor/Bachelor_Losey_Sylvain.pdf
#================================End of tutorial Links==================
# 06-Nov-2019
from bs4 import BeautifulSoup
import requests
import csv


soup = BeautifulSoup(source, 'lxml')

csv_file = open('web_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','Summary','Video_Link'])


# print(soup.prettify())
for article in soup.find_all('article'):
    # print(article.prettify())
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        # print(vid_src)
        vid_id = vid_src.split('/')[4] #item on index 4
        #print(vid_id)
        vid_id = vid_id.split('?')[0]
        # print(vid_id)
        youtube_link = f'https://www.youtube.com/watch?v={vid_id}'
        
    except Exception as e:

        youtube_link = None

    print(youtube_link)

    print()
    csv_writer.writerow([headline,summary,youtube_link])

csv_file.close()


