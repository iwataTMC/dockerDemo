from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.http import JsonResponse
from .forms import AjaxForm
from .models import GPS

class TopPage(FormView):
    # テンプレートの指定
    template_name = 'gps/top_page.html'
    # formの情報
    form_class = AjaxForm
    # form成功時の遷移先
    success_url = 'top_page'

    # post受信時
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)

        # formの情報が有効な場合
        if form.is_valid():
            # ajaxのリクエストの場合
            if request.is_ajax():
                # ajaxのレスポンスを取得
                data = form.ajax_response()
                # DB登録用のインスタンスを取得
                gps = form.save(commit=False)
                # 保存処理
                gps.save(latitude=data['latitude'], longitude=data['longitude'])
                response = JsonResponse(data)
            # ajax以外のリクエストの場合
            else:
                response = super().form_valid(form)
        # formの情報が無効な場合
        else:
            response = super().form_invalid()

        return response

    # get受信時に呼ばれるメソッドのオーバーライド
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # タイトルの設定
        context['title'] = 'Leaflet + OpenStreetMap'
        # 初期の位置情報の設定
        context['position'] = {'latitude': 35.4135, 'longitude': 135.0111}

        return context

class GPShistory(ListView):
    model = GPS
    context_object_name = 'gps_histories'
    template_name = 'gps/history.html'
    paginate_by = 20
