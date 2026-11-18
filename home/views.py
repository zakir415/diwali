from django.shortcuts import render,redirect
from .forms import CrackerForm
from .models import Crackers
# Create your views here.
def add_crackers(request):
    form = CrackerForm()
    if request.method == "POST":
        form = CrackerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # print("hello")
            return redirect("crack")
    context = {
        'form':form
    }
    return render(request,'crack.html',context)

def home(request):
    data = Crackers.objects.all()
    context = {
        'data':data
    }
    return render(request,"home.html",context)
