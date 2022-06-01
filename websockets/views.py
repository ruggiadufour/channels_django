from django.shortcuts import render

def index(request):
    return render(request, 'noti/notification.html', {})

def noti(request, room_name):
    return render(request, 'noti/notification.html', {
        'room_name': room_name
    })