from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def list_taxpayer(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'taxpayer/templates/index.html', context)


def create_taxpayer(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taxpayer')
    else:
        initial_data = {'username': '', 'email': '', 'password1': '', 'password2': ''}
        form = UserCreationForm(initial=initial_data)

    context = {'user': form}
    return render(request, 'taxpayer/templates/create.html', context)


def update_taxpayer(request, pk):
    taxpayer = User.objects.get(id=pk)

    form = UserCreationForm(instance=taxpayer)

    if request.method == "POST":
        form = UserCreationForm(request.POST, instance=taxpayer)
        if form.is_valid():
            form.save()
            return redirect('taxpayer')

    context = {'form': form, 'id': pk}
    return render(request, 'taxpayer/templates/update.html', context)


def delete_taxpayer(request, pk):
    taxpayer = User.objects.get(id=pk)
    taxpayer.delete()

    return redirect('taxpayer')
