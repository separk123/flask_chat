import os
# json으로 바꾸기 위해 라이브러리 추가
import json
from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return '챗봇페이지입니다'
    
@app.route("/keyboard")
def keyboard():
    
    # keyboard 딕셔너리 생성
    keyboard = {
      "type" : "buttons",
     "buttons" : ["메뉴", "로또", "고양이", "영화"]
}
    # 딕셔너리를 json으로 바꿔서 리턴해주기 위한 코드
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
