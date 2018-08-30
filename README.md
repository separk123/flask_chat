# 파이썬 챗봇 만들기

### 카카오톡 플러스 친구 관리자 센터

- 플러스 친구 생성 후 공개설정 (공개 안 하면 검색 불가)
- 스마트 챗팅 API형 사용

### C9 개발

- 우측 상단의 톱니바퀴에 들어가서 python3로 설정 변경
- `sudo pip3 install flask` 플라스크 설치

### keyboard

```python3
import os
import json
from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return '챗봇페이지입니다'
    
@app.route("/keyboard")
def keyboard():
    keyboard = {
      "type" : "buttons",
     "buttons" : ["메뉴", "로또", "고양이", "영화"]
}
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
```

