from flask import Flask, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/user/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def hello_world():
    data = {
        'success': True,
        'code': 20000,
        'message': '成功',
        'data':{'token1': 'admin'}
    }

    return jsonify(data)


@app.route('/user/info', methods=['GET'])
@cross_origin(supports_credentials=True)
def hello_world1():
    data = {
        'code': 20000,
        'message': '成功',
        'data': {'name': 'admin', 'roles': ['admin', 'admin']}
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
