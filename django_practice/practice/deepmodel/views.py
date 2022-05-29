from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'deepmodel/index.html')

def room(request, room_name):
    return render(request, 'deepmodel/room.html', {
        'room_name': room_name
    })