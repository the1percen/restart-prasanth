from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Table 
from .forms import ReserveForm 
# Create your views here

def index(request):
    return render(request, "index.html")

def table_list(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            table_id = form.cleaned_data['reserved_table']
            return redirect('table_list') 
    else:
        form = ReserveForm()
    tables = Table.objects.all()
    return render(request, 'table_list.html', {'tables': tables, 'reserve_form': form})
