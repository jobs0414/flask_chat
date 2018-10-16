import os
#json으로 바꾸기 위해 라이브러리 추가
import json
import random
import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import scrapy


app = Flask(__name__)

@app.route('/')
def hello():
    return '챗봇페이지 입니다!!!!'
    
@app.route('/keyboard')
def keyboard():
    
    #keyboard 딕셔너리 생성
    keyboard = {
      "type" : "buttons",

      "buttons" : ['로또', "영화", "메뉴", "고양이","강아지","날씨","증권","웹툰"]

    #딕셔너리를 json으로 바꿔서 리턴 해주기 위한 코드
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    

@app.route('/message', methods=['POST'])
def message():
    
    # content라는 key의 value를 msg에 저장
    msg = request.json['content']
    img_bool = False
    if msg == "점심메뉴":
    
        menu = ['버거킹','돈까스','중국집','한식','일식','백반정식','굶자','스파게티','김밥천국','구내식당','편의점','서브웨이']

    elif msg == "회식메뉴"

        menu = ['삼겹살+소맥','곱창집','비어맥주','']

        return_msg = random.choice(menu)
    elif msg == "로또":
    #     # 1~45 리스트 
    #     numbers1 = list(range(1,46))
    #     numbers2 = list(range(1,46))
    #     numbers3 = list(range(1,46))
    #     # 6개 샘플링
    #     pick = random.sample(numbers1, 6)
    #     pick2 = random.sample(numbers2, 6)
    #     pick3 = random.sample(numbers3, 6)
    #     # 정렬 후 스트링으로 변환 하여 저장
    #     return_msg = str(sorted(pick))
    #     return_msg2 = str(sorted(pick2))
    #     return_msg3 = str(sorted(pick3))

   
    # elif msg == "고양이":
    #     img_bool = True
    #     url = "https://api.thecatapi.com/v1/images/search?mime_types=image/gif"
    #     req = requests.get(url).json()
    #     return_msg = "나만 고양이 없어 :("
    #     img_url = req[0]['url']
 
 
    # elif msg == "강아지":
    #     img_bool = True
    #     url = "https://dog.ceo/api/breeds/image/random"
    #     req = requests.get(url).json()
    #     return_msg = "나만 강아지 없어 :("
    #     img_url = req['message']
   
 
    elif msg == "영화":
        img_bool = True
        url = "https://movie.naver.com/movie/running/current.nhn"
        req = requests.get(url).text
        
        doc = BeautifulSoup(req, 'html.parser') 
        
        title_tag = doc.select('dt.tit > a')
        star_tag = doc.select('div.star_t1 > a > span.num')
        reserve_tag = doc.select('div.star_t1.b_star > span.num')
        img_tag = doc.select('div.thumb > a > img')


        
        movie_dic = {}
        for i in range(0,10):
            movie_dic[i] = {
                "title":title_tag[i].text,
                "star":star_tag[i].text,
                "reserve":reserve_tag[i].text,
                "img":img_tag[i].get('src')
            }
            
        # pick_movie = movie_dic[random.randrange(0,10)]
        
        return_msg = "%s/평점:%s/예매율:%s" % (movie_dic['title'],movie_dic['star'],movie_dic['reserve'])
        img_url = movie_dic['img']
 
    else:
        return_msg = "현재 메뉴만 지원합니다 :)"
    
    if img_bool == True:
        json_return = {
            "message": {
                "text": return_msg,
                "photo": {
                    "url": img_url,
                    "width":720,
                    "height":600
                }
            },
            "keyboard": {
              "type" : "buttons",

              "buttons" : ['로또', "영화", "메뉴", "고양이","강아지","날씨","증권","웹툰"]

            }
        }
    else:
        json_return = {
            "message": {
                "text": return_msg
            },
            "keyboard": {
              "type" : "buttons",

              "buttons" : ['로또', "영화", "메뉴", "고양이","강아지","날씨","증권","웹툰"]

            
            }
        }
        
    return jsonify(json_return)
    
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))