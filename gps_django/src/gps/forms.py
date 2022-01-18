from django import forms
import json
import random
import os

class AjaxForm(forms.Form):
    # ajaxのレスポンスの生成
    def ajax_response(self):
        # ファイルを読み込む
        file_path = os.path.join('gps', 'gps.json')
        with open(file_path, 'r') as fin:
            inputs = json.load(fin)
        # リストに変換
        data = [value for value in inputs.values()]
        # 適当にデータを取り出す
        response = data[random.randrange(len(data))]

        return response
