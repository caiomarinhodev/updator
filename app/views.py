import time
from threading import Thread

import requests
from django.views.generic import TemplateView


def access_request(url, timer):
    while True:
        url = str(url)
        timer = int(timer)
        req = requests.get(url)
        if req.status_code == 404:
            print('TUDO OK em: ', url)
        else:
            print('Erro ao acessar URL: ', url)
        time.sleep(timer)


class IndexSite(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        Thread(target=access_request, kwargs=dict(url='http://updator1.herokuapp.com/', timer=900)).start()
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
