import os
#json으로 바꾸어주기 위한 라이브러리 추가 
import json
import random
from flask import Flask, request ,jsonify


app=Flask(__name__)

@app.route('/')
def hello(): 
    return '챗봇 페이지 입니다!!!!'
    
@app.route('/keyboard')
def keyboard(): 
    
    #keyboard 딕셔너리 생성 
    keyboard= {
       "type" : "buttons",
       "buttons" : ["메뉴", "로또", "고양이","영화"]
    }

    #딕셔너리를 json으로 바꿔서 리턴 해주기 위한 코드 
    json_keyboard= json.dumps(keyboard)
    return json_keyboard
    
    
@app.route('/message',methods=['POST'])
def message(): 
    
    # content라는 key의 value를 msg에 저장 
    msg= request.json['content']
    lot= request.json['content']

    if msg == "메뉴": 
        menu=["20층","멀캠식당","급식","꼭대기"]
        return_msg= random.choice(menu)
  
      elif msg =="로또": 
        #1~45 리스트 
        numbers=list(range(1,46))
        #6개 샘플링 
        pick=random.sample(numbers,6)
        #정렬 후 스트링으로 변환 후 
        return_msg=str(sorted(pick))
        
  
  
  
    else : 
        return_msg = "현재 메뉴만 지원합니다"




   # if lot =="로또": 
    #    lotto=random.sample(range(1,46),6)
     #   return_lot= int(lotto)
        
    #else : 
     #   return_lot = 
      #  "로또 랜덤번호 추출!"
        

    json_return = {
        "message":{
            "text":return_msg    
            
        },
        
        "keyboard":  {
            "type" : "buttons",
            "buttons" : ["메뉴", "로또", "고양이","영화"]
          }
        
    }
    
    return jsonify(json_return)


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    

