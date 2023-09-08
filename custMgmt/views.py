from django.shortcuts import render, redirect
from custMgmt.models import Customer
from custMgmt.forms import CustomerForm
from django.http import HttpResponse
# Create your views here.
def getCustomer(request):
    customers = Customer.objects.all()
    return render(request, 'allCustomers.html', {'customers':customers})

def addCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Invalid data")
        return redirect('/')
    return render(request, 'addCustomer.html', {'form':form})

def deleteCustomer(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('/')

def updateCustomer(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'updateCustomer.html', {'form':form})

def search_feature(request):
    if request.method == "POST":
        search_query = request.POST['search_query']
        searched_data = Customer.objects.filter(firstName__contains=search_query)
        print(searched_data)
        return render(request, 'search_result.html', {'searched_data':searched_data, 'search_query':search_query})
    else:
        return HttpResponse("No Data Found")

