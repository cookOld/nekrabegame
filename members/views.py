from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from accounts.models import Profile

def index(request):
    return member(request, request.user.id)
def users(request):
    profiles = Profile.objects.all()
    context = {
        'profiles':profiles,
    }
    return render(request, 'members/users.html', context)
def member(request, pk):
    if request.user.is_authenticated:
        if int(request.user.id) == int(pk):
            try:
                user = Profile.objects.get(user_id=int(pk))
                return render(request, 'members/member.html', {'profile':user, 'a':True})
            except  Profile.DoesNotExist:
                return redirect('/')
        else:
            try:
                user = Profile.objects.get(user_id=int(pk))
                return render(request, 'members/member.html', {'profile':user, 'a':False})
            except  Profile.DoesNotExist:
                return redirect('/')
    else:
        try:
            user = Profile.objects.get(user_id=int(pk))
            return render(request, 'members/member.html', {'profile':user, 'a':False})
        except  Profile.DoesNotExist:
            return redirect('/')