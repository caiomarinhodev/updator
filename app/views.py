import time
from threading import Thread

import requests
from django.views.generic import TemplateView


def access_request(url, timer):
    while True:
        url = str(url)
        timer = int(timer)
        req = requests.get(url)
        if req.status_code == 200:
            print('TUDO OK em: ', url)
        else:
            print('Erro ao acessar URL: ', url)
        time.sleep(timer)


class IndexSite(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        Thread(target=access_request,
               kwargs=dict(url='http://tvmovel.herokuapp.com/collect-multicanais/', timer=1200)).start()
        Thread(target=access_request, kwargs=dict(url='http://updator2.herokuapp.com/', timer=60)).start()
        return super(IndexSite, self).get(request, *args, **kwargs)
