from flask import render_template
import requests
from IPython.display import Audio
def Trang_chu():
    return render_template("index.html")

API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-vie"
headers = {"Authorization": "Bearer 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"}
def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
def create_sound(text):
    try:
        if(text=="" or text==None):
            audio_bytes = query({
            "inputs": "bạn chưa nhập kí tự nào cả",
        })
        else: 
            audio_bytes = query({
                "inputs": text,
            })
        if audio_bytes == "b'Internal Server Error'":
            print("err_1")
            create_sound("bạn chưa nhập kí tự nào cả") 
        audio = Audio(audio_bytes)
        with open('./static/audio.mp3', 'wb') as f:
            f.write(audio.data)
    except():
        create_sound("lỗi khi chuyển đổi thành âm thanh")



def conv_vie(key_word,m):
    if len(m)>0:
        if key_word=="^":
            if m[-1]=="a":
                m=m[:len(m)-1]
                m+="â"
                return m
            elif m[-1]=="e":
                m=m[:len(m)-1]
                m+="ê"
                return m
            elif m[-1]=="o":
                m=m[:len(m)-1]
                m+="ô"
                return m
            else:
                return m
        elif key_word=="@":
            if m[-1]=="a":
                m=m[:len(m)-1]
                m+="ă"
                return m
            else:
                return m
        elif key_word==",":
            if m[-1]=="o":
                m=m[:len(m)-1]
                m+="ơ"
                return m
            elif m[-1]=="u":
                m=m[:len(m)-1]
                m+="ư"
                return m
            else:
                return m
        elif key_word=="/":
            if m[-1]=="a":
                m=m[:len(m)-1]
                m+="á"
                return m
            elif m[-1]=="ă":
                m=m[:len(m)-1]
                m+="ắ"
                return m
            elif m[-1]=="â":
                m=m[:len(m)-1]
                m+="ấ"
                return m
            elif m[-1]=="e":
                m=m[:len(m)-1]
                m+="é"
                return m
            elif m[-1]=="ê":
                m=m[:len(m)-1]
                m+="ế"
                return m
            elif m[-1]=="u":
                m=m[:len(m)-1]
                m+="ú"
                return m
            elif m[-1]=="ư":
                m=m[:len(m)-1]
                m+="ứ"
                return m
            elif m[-1]=="o":
                m=m[:len(m)-1]
                m+="ó"
                return m
            elif m[-1]=="ô":
                m=m[:len(m)-1]
                m+="ố"
                return m
            elif m[-1]=="ơ":
                m=m[:len(m)-1]
                m+="ớ"
                return m
            else:
                return m
        elif key_word=="\\":
            if m[-1]=="a":
                m=m[:len(m)-1]
                m+="à"
                return m
            elif m[-1]=="ă":
                m=m[:len(m)-1]
                m+="ằ"
                return m
            elif m[-1]=="â":
                m=m[:len(m)-1]
                m+="ầ"
                return m
            elif m[-1]=="e":
                m=m[:len(m)-1]
                m+="è"
                return m
            elif m[-1]=="ê":
                m=m[:len(m)-1]
                m+="ề"
                return m
            elif m[-1]=="u":
                m=m[:len(m)-1]
                m+="ù"
                return m
            elif m[-1]=="ư":
                m=m[:len(m)-1]
                m+="ừ"
                return m
            elif m[-1]=="o":
                m=m[:len(m)-1]
                m+="ò"
                return m
            elif m[-1]=="ô":
                m=m[:len(m)-1]
                m+="ồ"
                return m
            elif m[-1]=="ơ":
                m=m[:len(m)-1]
                m+="ờ"
                return m
            else:
                return m
        elif key_word=="?":
            if m[-1]=="a":
                m=m[:len(m)-1]
                m+="ả"
                return m
            elif m[-1]=="ă":
                m=m[:len(m)-1]
                m+="ẳ"
                return m
            elif m[-1]=="â":
                m=m[:len(m)-1]
                m+="ẩ"
                return m
            elif m[-1]=="e":
                m=m[:len(m)-1]
                m+="ẻ"
                return m
            elif m[-1]=="ê":
                m=m[:len(m)-1]
                m+="ể"
                return m
            elif m[-1]=="u":
                m=m[:len(m)-1]
                m+="ủ"
                return m
            elif m[-1]=="ư":
                m=m[:len(m)-1]
                m+="ử"
                return m
            elif m[-1]=="o":
                m=m[:len(m)-1]
                m+="ỏ"
                return m
            elif m[-1]=="ô":
                m=m[:len(m)-1]
                m+="ổ"
                return m
            elif m[-1]=="ơ":
                m=m[:len(m)-1]
                m+="ở"
                return m
            else:
                return m
        elif key_word=="~":
            if m[-1]=="a":
                m=m[:len(m)-1]
                m+="ã"
                return m
            elif m[-1]=="ă":
                m=m[:len(m)-1]
                m+="ẵ"
                return m
            elif m[-1]=="â":
                m=m[:len(m)-1]
                m+="ẫ"
                return m
            elif m[-1]=="e":
                m=m[:len(m)-1]
                m+="ẽ"
                return m
            elif m[-1]=="ê":
                m=m[:len(m)-1]
                m+="ễ"
                return m
            elif m[-1]=="u":
                m=m[:len(m)-1]
                m+="ũ"
                return m
            elif m[-1]=="ư":
                m=m[:len(m)-1]
                m+="ữ"
                return m
            elif m[-1]=="o":
                m=m[:len(m)-1]
                m+="õ"
                return m
            elif m[-1]=="ô":
                m=m[:len(m)-1]
                m+="ỗ"
                return m
            elif m[-1]=="ơ":
                m=m[:len(m)-1]
                m+="ỡ"
                return m
            else:
                return m
        elif key_word==".":
            if m[-1]=="a":
                m=m[:len(m)-1]
                m+="ạ"
                return m
            elif m[-1]=="ă":
                m=m[:len(m)-1]
                m+="ặ"
                return m
            elif m[-1]=="â":
                m=m[:len(m)-1]
                m+="ậ"
                return m
            elif m[-1]=="e":
                m=m[:len(m)-1]
                m+="ẹ"
                return m
            elif m[-1]=="ê":
                m=m[:len(m)-1]
                m+="ệ"
                return m
            elif m[-1]=="u":
                m=m[:len(m)-1]
                m+="ụ"
                return m
            elif m[-1]=="ư":
                m=m[:len(m)-1]
                m+="ự"
                return m
            elif m[-1]=="o":
                m=m[:len(m)-1]
                m+="ọ"
                return m
            elif m[-1]=="ô":
                m=m[:len(m)-1]
                m+="ộ"
                return m
            elif m[-1]=="ơ":
                m=m[:len(m)-1]
                m+="ợ"
                return m
            else:
                return m
        elif key_word=="ok":
            return m+"_"
        elif key_word=="space":
            return m+" "
        elif key_word=="delete":
            m=m[:len(m)-1]
            return m
    elif(key_word=="space"):return m
    elif(key_word=="ok"):return m
    elif(key_word=="delete"):return m
    elif(key_word=="^"):return m
    elif(key_word==","):return m
    elif(key_word=="@"):return m
    elif(key_word=="?"):return m
    elif(key_word=="~"):return m
    elif(key_word=="."):return m
    elif(key_word=="/"):return m
    elif(key_word=="\\"):return m
    return m+key_word
