from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, 'dispatch')
class HookView(View):
    def post(self, request):
        if request.headers.get('X-GitHub-Event'):
            return HttpResponse('pong', content_type='text/plain')
        return HttpResponse('Ok', content_type='text/plain')
