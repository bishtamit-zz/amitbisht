from django.shortcuts import render, redirect, reverse
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import UserForm, User, ProfileForm
from django.urls import reverse_lazy


# Create your views here.
# @login_required
# @transaction.atomic
def profile_view(request):
    return render(request, 'profiles/profile.html')


@login_required(login_url=reverse_lazy('account:login'))
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profiles:profile')
        else:
            pass
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
