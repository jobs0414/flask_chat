import requests
from bs4 import BeatifulSoup


url="https://movie.naver.com/movie/running/current.nhn"
req= requests.get(url).text 



doc=BeatifulSoup(req,'html.parser')

title_dog = doc.select('dt.tit>a')
star_tag = doc.select('div.star_t1> a > span.num')
reserve_tag = doc.select('div')

img_tag = doc.select('div.thumb > a > img')





movie_dic = {} 

for i in range(0,10):
    movie_dic[i]= { 
        "title":title_tag[i].text, 
        "star": star_tag[i].text,
        "reserve":reserve_tag[i].text
        "img": img_tag[i].get['src']
    } 
    
    pick_movie = movie_dic[random.randrange(0,10)]
    print(pick_movie)
    
    
    
    
    
    
    
    print(title[i])
    print(star_tag[i])
    print(reserve_tag[i].text)
print(len(title_dog))
print(len(star_tag))
