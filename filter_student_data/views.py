from django.shortcuts import render,redirect
from .models import StudetData
# Create your views here.

info = None

def index(request):
    if request.method == 'POST':
        from_std = request.POST.get('from_std')
        to_std = request.POST.get('to_std')
        name = request.POST.get('name')
        age = request.POST.get('age')
        roll_no = request.POST.get('roll_no')
        std = request.POST.get('std')
        mobile_num = request.POST.get('mble_no')
        
        print(to_std,from_std,name,age,roll_no)
        lst = []
        if name != 'on':
            lst.append('name')
        if age != 'on':
            lst.append('age')
        if roll_no != 'on':
            lst.append('roll_no')
        if std != 'on':
            lst.append('standard')
        if mobile_num != 'on':
            lst.append('mobile_no_p1')
            lst.append('mobile_no_p2')
        
        print(lst)
    
        if from_std>to_std:
            fetch_data = StudetData.objects.filter(standard__range=[to_std,from_std])
        else:
            fetch_data = StudetData.objects.filter(standard__range=[from_std,to_std])

        print(fetch_data)
        global info
        info = fetch_data
        return redirect(data,lst)
        
    else:
        return render(request,'index.html')




def data(request,lst):
    global info
    print(lst)
    return render(request, 'data.html', {'data':info,'exclude':lst})