from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            new_user.refresh_from_db()

            new_profile = Profile()
            new_profile.user = new_user
            new_profile.photo = request.FILES['photo']
            new_profile.phone = request.POST['phone']
            new_profile.gender = request.POST['gender']
            new_profile.org = request.POST['org']
            new_profile.job = request.POST['job']
            new_profile.save()
            new_user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'],)
            login(request, new_user)
            return redirect('/members/')
    return render(request, 'accounts/sign.html')