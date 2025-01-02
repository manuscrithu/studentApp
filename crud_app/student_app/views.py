from django.shortcuts import render, redirect, get_object_or_404
from .forms import datain, search, update
from .models import student
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# view all
def app(request):
    children = student.objects.all()
    return render(request, 'app.html', { "children" : children })

# data inserting
def dataForm(request):
    if request.method == "POST":
        form = datain(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app')
    else:
        form = datain()
    return render(request, 'datain.html', {"form": form})

# view single instance
def view_child(request, nic):
    child = student.objects.get(nic=nic)
    return render(request, 'child.html', { "child" : child })

# search instances
def item_search(request):
    form = search(request.GET or None)
    results = []
    
    if form.is_valid():
        nic = form.cleaned_data.get('nic')
        name = form.cleaned_data.get('name')
        resident = form.cleaned_data.get('resident')
        
        # Build the query dynamically
        queryset = student.objects.all()
        if nic:
            queryset = queryset.filter(nic__icontains=nic)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if resident:
            queryset = queryset.filter(resident__icontains=resident)
        
        results = queryset

    return render(request, 'search.html', {'form': form, 'results': results})

# update instance
def item_update(request, pk):
    child = get_object_or_404(student, pk=pk)  # Get the student record by primary key (pk)
    
    if request.method == 'POST':
        form = update(request.POST, instance=child)
        if form.is_valid():
            form.save()  # Save the updated student record
            return redirect('child', nic=child.nic)  # Redirect to the child's detail page
    else:
        form = update(instance=child)  # Pre-fill the form with existing student data

    return render(request, 'update.html', {'form': form, 'child': child})

# delete instance
def item_delete(request, pk):
    child = get_object_or_404(student, pk=pk)
    if request.method == 'POST':  # Confirm delete
        child.delete()  # Deletes the student record
        return redirect('app')
    return render(request, 'delete.html', {'child': child})


# user creation form
def createUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("app")
    else:
        form = UserCreationForm()
    return render(request, "create_user.html", { "form" : form })


# user login
def log_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Set session expiry to persist after the browser is closed
            request.session.set_expiry(None)
            return redirect("app")
    else:
        form = AuthenticationForm()
    return render(request, "log_user.html", { "form": form })


# logout
def logout_user(request):
    logout(request)  # Log out the user
    return redirect("login")  # Redirect to the login page or any other page