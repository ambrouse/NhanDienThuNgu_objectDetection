from flask import Flask,session,render_template,request
from flask_socketio import SocketIO
import index
import cv2
import base64
from ultralytics import YOLO
import time
import os

app = Flask(__name__,template_folder="view")
# conect socketIO
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='threading', manage_session=False)
debug_ok = True
m = ''
check = True
@socketio.on('on_camera')
def create_img_api(key):
    if key=="turn_on":
        global check
        global m
        global debug_ok
        m=''
        check=True
        link_model = r"C:\Users\LymI\Desktop\New folder\app\model\best.pt"
        model = YOLO(link_model)
        curentime = time.time()
        time_step = time.time()
        time_num = 0.5
        check_ = True
        vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while(check):
            # on camera
            ret, frame = vid.read()
            # predict and draw box
            img=frame.copy()   
            detect_ob = model(frame)
            class_ = detect_ob[0].boxes.cls
            xyxy = detect_ob[0].boxes.xyxy
            name = model.names
            if class_ is not None:
                for index__,i in enumerate(xyxy):
                        img = cv2.rectangle(img,(int(xyxy[index__][0]),int(xyxy[index__][1])),(int(xyxy[index__][2]),int(xyxy[index__][3])), (0,0,255),thickness=2)
                        break
            # give socket display html
            img = cv2.imencode('.jpg',img)[1]
            img = base64.b64encode(img).decode('utf8')
            socketio.emit("get_img",img)
            # delay time predict
            if check_==True:
                if curentime-time_step<time_num:
                    curentime=time.time()
                    socketio.emit("get_deley_time","OFF")
                    continue
                else:
                    check_=False
            socketio.emit("get_deley_time","ON")
            if len(class_)>0 and debug_ok:
                time_step=time.time()
                curentime=time.time()
                check_=True
                key_word = str(name[int(class_[0])])
                # check keyword - delete - space...
                m = index.conv_vie(key_word=key_word,m=m)
                socketio.emit("get_text",str(m))
            else:
                time_step=time.time()
                check_=True
        vid.release()
        cv2.destroyAllWindows()
        return socketio.emit("get_not_img","Đã tắt Camera!"),socketio.emit("get_deley_time","OFF")
    
    if key=="turn_of":
        check=False

@app.route('/',methods=['POST','GET'])
def home():
    return index.Trang_chu()
@socketio.on('debug_ok_')
def debug_ok_(text):
    global debug_ok
    if text=="no":
        debug_ok=False
    else:
        debug_ok=True
        global m
        m=''
@socketio.on('phat_thanh')
def phatthanh(text):
    index.create_sound(text)
    socketio.emit("audio_complete",text)
@socketio.on('delete_')
def delete_(text):
    os.remove("static/audio.mp3")
    
@socketio.on('end_task')
def end_task(text):
    global m
    m=''
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=6969)
    socketio.run(app,host='0.0.0.0', port=9696)