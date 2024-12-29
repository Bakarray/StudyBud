from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': "Let's learn python"},
    {'id': 2, 'name': "Let's build projects"},
    {'id': 3, 'name': "Let's get money"}
]

# Function based view
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    current_room = None
    for room in rooms:
        if room['id'] == int(pk):
            current_room = room

    context = {'room': current_room}
    return render(request, 'base/room.html', context)