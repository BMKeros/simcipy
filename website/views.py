from django.shortcuts import render


def index_fronted(request):
    return render(request, 'index.html')
