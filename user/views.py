from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from .models import User

# Create your views here.

def home(request):
    users = User.objects.all()
    return render(request, 'user/home.html', {'users': users})

def ajouter_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        #request.session['ajout'] = True
        #return redirect('home')
        return render(request, 'user/home.html', {'users': User.objects.all(), 'ajout': True})
    return render(request, 'user/ajouter.html', locals())

def modifier_user(request, mail):
    user = get_object_or_404(User, mail=mail)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            #request.session['modif'] = True
            #return redirect('home')
        return render(request, 'user/home.html', {'users': User.objects.all(), 'modif': True})
    return render(request, 'user/modifier.html', locals())

def supprimer_user(request, mail):
    user = get_object_or_404(User, mail=mail)
    user.delete()
    #request.session['sup'] = True
    #return redirect('home')
    return render(request, 'user/home.html', {'users': User.objects.all(), 'sup': True})