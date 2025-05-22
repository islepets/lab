from django.shortcuts import render, get_object_or_404, redirect
from .models import Call
from .forms import CallForm

# Create your views here.


def call_list(request):
    calls = Call.objects.all()
    return render(request, 'calls/call_list.html', {'calls' : calls})

def call_create(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('call_list')
    else:
        form = CallForm
    return render(request, 'calls/call_form.html', {'form' : form})

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

def call_delete(request, pk):
    call = get_object_or_404(Call, pk=pk)
    if request.method == 'POST':
        call.delete()
        return redirect('call_list')
    return render(request, 'calls/call_confirm_delete.html', {'call': call})