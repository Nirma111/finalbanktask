from django.shortcuts import render
from .forms import CustomerForm
from django.contrib import messages
from . models import SubArea
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def postlogin(request):
    if request.method == 'POST':
        form =CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Application Accepted")

    else:
        form = CustomerForm()

    return render(request, 'postlogin.html', {'form': form})
def get_branches(request):
    district_id = request.GET.get('district_id')
    branches = SubArea.objects.filter(district_id=district_id).all()
    print(list(branches.values('id', 'name')))
    return JsonResponse(list(branches.values('id', 'name')),safe=False)



