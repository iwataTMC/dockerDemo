from flask import Flask, jsonify, render_template
import json
import random
app = Flask(__name__)

# top page
@app.route('/', methods=['GET'])
def top_poge():
    # ファイルから読み込む
    with open('geo.json', 'r') as fin:
        data = json.load(fin)
    position = '日本標準時子午線'

    return render_template('top_page.html', title='Top Page', position=position, geo=data)

# reload
@app.route('/update', methods=['GET'])
def update():
    # 名古屋城の緯度・経度
    data = {
        'latitude':   35.1855875,
        'longitude': 136.8990919,
    }
    position = '名古屋城の緯度・経度'

    return render_template('top_page.html', title='Top Page', position=position, geo=data)

# ajax
@app.route('/get_geography', methods=['POST'])
def get_geography():
    information = [
        # 厳島神社の緯度・経度
        {
            'name': '厳島神社',
            'latitude':   34.2947561,
            'longitude': 132.3185929,
        },
        # 東京タワー
        {
            'name': '東京タワー',
            'latitude':    35.658584,
            'longitude': 139.7454316,
        },
        # 札幌時計台
        {
            'name': '札幌時計台',
            'latitude':   43.0631159,
            'longitude': 141.3534520,
        },
        # 首里城
        {
            'name': '首里城',
            'latitude':   26.2170853,
            'longitude': 127.7194279,
        },
    ]
    # 乱数で適当にデータを選択
    data = information[random.randrange(len(information))]
    response = {
        'Content-Type': 'application/json',
        'geography': data,
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8780, threaded=True)
