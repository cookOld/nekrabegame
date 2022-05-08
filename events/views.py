from django.shortcuts import render, redirect
from .models import Event, E_request
from accounts.models import Profile
import datetime

def index(request):
    events = Event.objects.all().order_by('date')
    now = datetime.date.today()
    for event in events:
        event.days =  event.date - now
        if event.days.days < 0 and event.status == "0":
            event.status = "2"
            event.save()
        elif event.days.days > 0:
            if event.days.days % 10 == 1 and event.days.days % 100 !=11:
                event.wait = "Остался "+ str(event.days.days)  +" день"
            elif 2 <= event.days.days % 10 <= 4 and (event.days.days % 100 < 10 or event.days.days % 100 >= 20):
                event.wait = "Осталось "+ str(event.days.days)  +" дня"
            else:
                event.wait = "Осталось "+ str(event.days.days)  +" дней"
        else:
            event.wait = "Сегодня"
    return render(request, 'events/index.html',{'events':events})
    
def info(request, pk):
    event = Event.objects.get(id=int(pk))
    profile = Profile.objects.get(user_id=event.user_id)
    ee_request = E_request.objects.all().filter(event_id = int(pk))
    request_count = 0
    for ee_reques in ee_request:
        if ee_reques.permission == 1:
            request_count += 1
    a = False
    q = ""
    d = 0
    u = {}
    if request.GET.get('q'):
        q = request.GET["q"]
    if request.user.is_authenticated:
        if request.user.id == event.user_id:
            a = True
        else:
            try:
                e_request = E_request.objects.all().filter(event_id = int(pk))
                for ei in e_request:
                    if ei.user_id == request.user.id and ei.permission == 1:
                        d = 1
                    if ei.user_id == request.user.id and ei.permission == 0:
                        d = 4
                if d == 0:
                    d = 2
            except:
                d = 2
    context = {
        'event': event,
        'profile': profile,
        'a':a,
        'q':q,
        'd':d,
        'request_count':request_count,
        'ee':ee_request,
        }
    return render(request, 'events/info.html', context)
def create(request):
    if request.method == 'POST':
        event = Event()
        event.title = request.POST["title"]
        event.desc = request.POST["desc"]
        event.x = request.POST["x"]
        event.y = request.POST["y"]
        event.acesss = request.POST["access"]
        event.event_type = request.POST["event_type"]
        event.user_id = request.user.id
        event.thumb = request.FILES['photo']
        event.start_time = request.POST["start_time"]
        event.end_time = request.POST["end_time"]
        event.date = request.POST["date"]
        event.status = "0"
        event.save()
        return redirect(f'/events/{event.id}')
    return render(request, 'events/create.html')
def e_request(request, pk):
    if request.method == 'POST':
        event = Event.objects.get(id=int(pk))
        e_request = E_request()
        e_request.event_id = event.id
        e_request.user_id = request.user.id
        if event.acesss == "0":
            e_request.permission = 1
        else:
            e_request.permission = 0
        e_request.save()
        return redirect('/events/' + str(event.id) + '/?q=1')
def delete(request, pk):
    event = Event.objects.get(id=int(pk))
    event.status = 2
    event.save()
    return redirect('/events/' + str(event.id))
def prof(request, pk):
    ee_request = E_request.objects.all().filter(event_id = int(pk))
    context = {
        'ee': ee_request,
        'pk': pk,
    }
    return render(request, 'events/prof.html', context)
def add(request, pk):
    ee_request = E_request.objects.get(id=int(request.POST['id']))
    ee_request.permission = 1
    ee_request.save()
    return redirect('/events/' + str(pk) + '/prof/')