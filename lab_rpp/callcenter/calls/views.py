from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from .models import Call, Client, Reason, Operator, Status
from .forms import CallForm, ClientForm, ReasonForm, OperatorForm, StatusForm, RegisterForm

def operator_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.has_perm('calls.view_call'):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.has_perm('calls.delete_call'):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

# Navigation
def home(request):
    return render(request, 'calls/home.html')

# Call views

def call_list(request):
    calls = Call.objects.all()
    return render(request, 'calls/call_list.html', {'calls': calls})

@manager_required
def call_create(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('call_list')
    else:
        form = CallForm()
    return render(request, 'calls/call_form.html', {'form': form})

@manager_required
def call_update(request, pk):
    call = get_object_or_404(Call, pk=pk)
    if request.method == 'POST':
        form = CallForm(request.POST, instance=call)
        if form.is_valid():
            form.save()
            return redirect('call_list')
    else:
        form = CallForm(instance=call)
    return render(request, 'calls/call_form.html', {'form': form})

@manager_required
def call_delete(request, pk):
    call = get_object_or_404(Call, pk=pk)
    if request.method == 'POST':
        call.delete()
        return redirect('call_list')
    return render(request, 'calls/call_confirm_delete.html', {'call': call})

# Client views
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'calls/client_list.html', {'clients': clients})

@manager_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'calls/client_form.html', {'form': form})

@manager_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'calls/client_form.html', {'form': form})

@manager_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'calls/client_confirm_delete.html', {'client': client})

# Reason views
def reason_list(request):
    reasons = Reason.objects.all()
    return render(request, 'calls/reason_list.html', {'reasons': reasons})

@manager_required
def reason_create(request):
    if request.method == 'POST':
        form = ReasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reason_list')
    else:
        form = ReasonForm()
    return render(request, 'calls/reason_form.html', {'form': form})

@manager_required
def reason_update(request, pk):
    reason = get_object_or_404(Reason, pk=pk)
    if request.method == 'POST':
        form = ReasonForm(request.POST, instance=reason)
        if form.is_valid():
            form.save()
            return redirect('reason_list')
    else:
        form = ReasonForm(instance=reason)
    return render(request, 'calls/reason_form.html', {'form': form})

@manager_required
def reason_delete(request, pk):
    reason = get_object_or_404(Reason, pk=pk)
    if request.method == 'POST':
        reason.delete()
        return redirect('reason_list')
    return render(request, 'calls/reason_confirm_delete.html', {'reason': reason})

# Operator views
def operator_list(request):
    operators = Operator.objects.all()
    return render(request, 'calls/operator_list.html', {'operators': operators})

@manager_required
def operator_create(request):
    if request.method == 'POST':
        form = OperatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operator_list')
    else:
        form = OperatorForm()
    return render(request, 'calls/operator_form.html', {'form': form})

@manager_required
def operator_update(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    if request.method == 'POST':
        form = OperatorForm(request.POST, instance=operator)
        if form.is_valid():
            form.save()
            return redirect('operator_list')
    else:
        form = OperatorForm(instance=operator)
    return render(request, 'calls/operator_form.html', {'form': form})

@manager_required
def operator_delete(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    if request.method == 'POST':
        operator.delete()
        return redirect('operator_list')
    return render(request, 'calls/operator_confirm_delete.html', {'operator': operator})

# Status views
def status_list(request):
    statuses = Status.objects.all()
    return render(request, 'calls/status_list.html', {'statuses': statuses})

@manager_required
def status_create(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = StatusForm()
    return render(request, 'calls/status_form.html', {'form': form})

@manager_required
def status_update(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = StatusForm(instance=status)
    return render(request, 'calls/status_form.html', {'form': form})

@manager_required
def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('status_list')
    return render(request, 'calls/status_confirm_delete.html', {'status': status})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'calls/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            operator_group = Group.objects.get(name='Оператор')
            user.groups.add(operator_group)

            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'calls/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

