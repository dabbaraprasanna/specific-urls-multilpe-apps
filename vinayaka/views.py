from django.shortcuts import render

# Create your views here.
def wednesday(request):
    return render(request,'wednesday.html')