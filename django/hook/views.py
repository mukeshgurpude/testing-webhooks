from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from subprocess import Popen, PIPE
from django.conf import settings
from os import getenv


@method_decorator(csrf_exempt, 'dispatch')
class HookView(View):
    def post(self, request):
        if request.headers.get('X-GitHub-Event') == 'ping':
            return HttpResponse('pong', content_type='text/plain')
        with open('data.json', 'w') as file:
            file.write(request.body.decode('utf-8'))
        Popen(('bash', settings.BASE_DIR/getenv('script')), stdout=PIPE)
        return HttpResponse('Ok', content_type='text/plain')
