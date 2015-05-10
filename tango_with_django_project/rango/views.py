from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'boldmessage': "Bold Messages",
    }
    return render(request,
                  'rango/index.html',
                  context
                  )


def about(request):
    return HttpResponse("About")
