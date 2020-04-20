from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    path_receive = request.form['path_give']
    content_receive = request.form['content_give']
    comment_receive = request.form['comment_give']

    review = {
        'path': path_receive,
        'content': content_receive,
        'comment': comment_receive
    }

    db.reviews.insert_one(review)
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'reviews': reviews})


@app.route('/reviews', methods=['DELETE'])
def delete_reviews():
    path_receive = request.form['path_give']
    content_receive = request.form['content_give']
    comment_receive = request.form['comment_give']

    # print(path_receive)
    # print(content_receive)
    # print(comment_receive)

    review = {
        'path': path_receive,
        'content': content_receive,
        'comment': comment_receive
    }

    db.reviews.delete_one(review)
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 삭제되었습니다.'})

    return "hi"

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
