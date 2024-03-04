import makePicture, time, os, threading
from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from gevent.pywsgi import WSGIServer
from winotify import Notification
from datetime import datetime

app = Flask(__name__)
CORS(app)

def write_log(text):
    now_time = time.strftime('%Y/%m/%d %H:%M:%S')
    with open('./logs/sendPost.log', "a+", encoding="utf-8") as f:
        f.write(f'[{now_time}] {text}\n')

def clean_log():
    while True:
        try:
            time.sleep(60)
            if os.stat('./logs/sendPost.log').st_size > 1024 * 1024 * 100:
                with open('./logs/sendPost.log', "w") as f:
                    f.write('')
                    write_log('Clean Log File Success')
        except FileNotFoundError:
            ...
        except Exception as e:
            print(e)
            
@app.route('/', methods=['GET'])
def home():
    return "ANJH NM API"

@app.route('/pending-review/', methods=['GET'])
def pending_review():
    count = 0
    for path in os.listdir("Z:\\ServerData"):
        if os.path.isfile(os.path.join("Z:\\ServerData", path)):
            count += 1
    return jsonify({'pendingReviewNumber': count - 1}), 200

@app.route('/send-post/', methods=['POST'])
@cross_origin()
def sendPost():
    ip = request.headers['CF-Connecting-IP'] if 'CF-Connecting-IP' in request.headers else request.remote_addr
    data = request.get_json()
    content = data['content']
    
    if len(content) > 200 or len(content) < 0:
        write_log(f"{ip}")
        return "", 400
    
    try:
        write_log(f"{ip} > {content}")
        unix = time.time()
        makePicture.write_pic(f"{content}", f"Z:\\ServerData\\{unix}.png")
        makePicture.write_pic(f"{content}", f"Z:\\ServerData\\AAA\\{unix}.png")
        toast = Notification(app_id="安南國中匿名平台", title="有人發送了一條匿名訊息", msg=f"{content}")
        toast.show()
        return "", 200
    except Exception as e:
        print(f"{e}")
        return "", 400

if __name__ == '__main__':
    try:
        print("Start Server")
        app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
        threading.Thread(target = clean_log).start()
        http_server = WSGIServer(('0.0.0.0', 5000), app)
        http_server.serve_forever()
    except KeyboardInterrupt:
        exit(0)
