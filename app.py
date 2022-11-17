from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient(
'mongodb+srv://test:sparta@cluster0.8d7bfaw.mongodb.net/?retryWrites=true&w=majority',
tlsCAFile = ca
)
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/visitor", methods=["POST"])
def YH_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.guest.insert_one(doc)
    return jsonify({'msg': '기록 완료!'})

@app.route("/visitor", methods=["GET"])
def homework_get():
    comment_list = list(db.guest.find({},{'_id':False}))
    return jsonify({'comments':comment_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)