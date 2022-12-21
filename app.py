import os
from PIL import Image
import requests
from io import BytesIO
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
import tweepy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
from werkzeug.utils import secure_filename

SECRET_KEY = "2*S28~NQ{p~c.aT"
UPLOAD_FOLDER = "C:/Users/tensor/Desktop/leaflet/static/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY

import base64

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/test', methods=["GET", "POST"])
def test():
    return render_template("test.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route("/twitter", methods=['GET', 'POST'])
@limiter.limit("100/day")
@limiter.limit("15/hour")
def twitter():
    if request.method == 'POST': 
        username = request.form.get('text')
        auth = tweepy.OAuthHandler("VkrreD50glR0MKTM60ds2twHd", "TfVrWJumsxTcK9Aj8UAbk9jeGxnoZGikNFY9beQEP4DxOShc87")
        auth.set_access_token("878974576570617856-mDJZap5Jy3OeS9TxoLcgII9z6TM7SH9", "4BgyiRsxxkORNe0FApchpFgVLUsjAb6HMPPojnbCJa4gq")
        api = tweepy.API(auth)
        user = None
        try:
                user = api.get_user(screen_name=username)
                print(user)
                 
        except tweepy.errors.TweepyException as e:
                flash("User not found")
                print(e)

                return render_template('index.html')
        else:  
                global user_profile_image
                user_profile_image = user.profile_image_url.replace('normal', '400x400')

        data1 = BytesIO()
        data2 = BytesIO()
        data3 = BytesIO()
        data4 = BytesIO()
        data5 = BytesIO()
        data6 = BytesIO()
        data7 = BytesIO()
        data8 = BytesIO()
        data9 = BytesIO()
        data10 = BytesIO()

        data11 = BytesIO()
        data12 = BytesIO()
        data13 = BytesIO()

        response = requests.get(user_profile_image)

        userimage1 = Image.open(BytesIO(response.content))
        #userimage1 = userimage1.resize((280,280),Image.ANTIALIAS)
        image1 = Image.open('static/img/nullframes/are_you_hired_son.png')
        userimage1.paste(image1, (0,0), image1)
        userimage1.save(data1, 'PNG', quality=100)
        img1 = base64.b64encode(data1.getvalue())

        userimage2 = Image.open(BytesIO(response.content))
        #image2 = userimage2.resize((280,280),Image.ANTIALIAS)
        image2 = Image.open('static/img/nullframes/blood_red.png')
        userimage2.paste(image2, (0,0), image2)
        userimage2.save(data2, 'PNG', quality=100)
        img2 = base64.b64encode(data2.getvalue())

        userimage3 = Image.open(BytesIO(response.content))
        #image3 = userimage3.resize((280,280),Image.ANTIALIAS)
        image3 = Image.open('static/img/nullframes/chroma.png')
        userimage3.paste(image3, (0,0), image3)
        userimage3.save(data3, 'PNG', quality=100)
        img3 = base64.b64encode(data3.getvalue())

        userimage4 = Image.open(BytesIO(response.content))
        #image4 = userimage4.resize((280,280),Image.ANTIALIAS)
        image4 = Image.open('static/img/nullframes/finedog.png')
        userimage4.paste(image4, (0,0), image4)
        userimage4.save(data4, 'PNG', quality=100)
        img4 = base64.b64encode(data4.getvalue())

        userimage5 = Image.open(BytesIO(response.content))
        #image5 = userimage5.resize((280,280),Image.ANTIALIAS)
        image5 = Image.open('static/img/nullframes/mini_world.png')
        userimage5.paste(image5, (0,0), image5)
        userimage5.save(data5, 'PNG', quality=100)
        img5 = base64.b64encode(data5.getvalue())

        userimage6 = Image.open(BytesIO(response.content))
        #image6 = userimage6.resize((280,280),Image.ANTIALIAS)
        image6 = Image.open('static/img/nullframes/party_hard.png')
        userimage6.paste(image6, (0,0), image6)
        userimage6.save(data6, 'PNG', quality=100)
        img6 = base64.b64encode(data6.getvalue())

        userimage7 = Image.open(BytesIO(response.content))
        #image7 = userimage7.resize((280,280),Image.ANTIALIAS)
        image7 = Image.open('static/img/nullframes/finedog.png')
        userimage7.paste(image7, (0,0), image7)
        userimage7.save(data7, 'PNG', quality=100)
        img7 = base64.b64encode(data7.getvalue())

        userimage8 = Image.open(BytesIO(response.content))
        #image8 = userimage8.resize((280,280),Image.ANTIALIAS)
        image8 = Image.open('static/img/nullframes/shootme.png')
        userimage8.paste(image8, (0,0), image8)
        userimage8.save(data8, 'PNG', quality=100)
        img8 = base64.b64encode(data8.getvalue())

        userimage9 = Image.open(BytesIO(response.content))
        #image9 = userimage9.resize((280,280),Image.ANTIALIAS)
        image9 = Image.open('static/img/nullframes/sunger.png')
        userimage9.paste(image9, (0,0), image9)
        userimage9.save(data9, 'PNG', quality=100)
        img9 = base64.b64encode(data9.getvalue())

        userimage10 = Image.open(BytesIO(response.content))
        #image10 = userimage10.resize((280,280),Image.ANTIALIAS)
        image10 = Image.open('static/img/nullframes/natural.png')
        userimage10.paste(image10, (0,0), image10)
        userimage10.save(data10, 'PNG', quality=100)
        img10 = base64.b64encode(data10.getvalue())

        userimage11 = Image.open(BytesIO(response.content))
        #image11 = userimage11.resize((280,280),Image.ANTIALIAS)
        image11 = Image.open('static/img/nullframes/finedog_s.png')
        userimage11.paste(image11, (0,0), image11)
        userimage11.save(data11, 'PNG', quality=100)
        img11 = base64.b64encode(data11.getvalue())

        userimage12 = Image.open(BytesIO(response.content))
        #image8 = userimage12.resize((280,280),Image.ANTIALIAS)
        image12 = Image.open('static/img/nullframes/shootme_s.png')
        userimage12.paste(image12, (0,0), image12)
        userimage12.save(data12, 'PNG', quality=100)
        img12 = base64.b64encode(data12.getvalue())

        userimage13 = Image.open(BytesIO(response.content))
        #image9 = userimage13.resize((280,280),Image.ANTIALIAS)
        image13 = Image.open('static/img/nullframes/sunger_s.png')
        userimage13.paste(image13, (0,0), image13)
        userimage13.save(data13, 'PNG', quality=100)
        img13 = base64.b64encode(data13.getvalue())

    return render_template('processing.html' , filename=user_profile_image, are_you_hired_son=img1.decode('utf-8'), blood_red=img2.decode('utf-8'), chroma=img3.decode('utf-8'), mini_world=img5.decode('utf-8'), nature=img10.decode('utf-8'), party_hard= img6.decode('utf-8'), finedog=img7.decode('utf-8'), shootme=img8.decode('utf-8'), sunger=img9.decode('utf-8'), finedog_s=img11.decode('utf-8'), shootme_s=img12.decode('utf-8'), sunger_s=img13.decode('utf-8'))

@app.route("/processing", methods=['GET', 'POST'])
def processing():
    return render_template('processing.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
