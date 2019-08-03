from django.shortcuts import render,HttpResponse
from .models import *
import csv
# Create your views here.
def search_status(request):

    if request.method == "GET":

        search_text= request.GET.get('search_text')


        if search_text is not None and search_text != u"":
            search_text = request.GET.get('search_text')
            statuss=pincode.objects.filter(Pincode__contains=search_text)
            #statuss = pincode.objects.filter(Village__icontains=search_text)
            #print(statuss,search_text)
        else:
            statuss = []




        return render(request, 'index.html', {'statuss':statuss})



def search(request):
    if request.method == 'GET':
        pinc = request.GET.get('searchpin')
        print(pinc)
        if pinc is not None:
            pins=pincode.objetcs.all()
            #pins = pincode.obejcts.all().filter(Village__icontains = pinc)
            print(pins)
            return render(request,'search.html',{'pins',pins})
        return render(request,'search.html')

    else:
        return render(request,'search.html')


'''def search_status2(request):

    if request.method == "GET":

        search_text= request.GET.get('search_text')

        print(search_text)
        # search_text = request.GET['search_text']
        if search_text is not None and search_text != u"":
            search_text = request.GET.['search_text']
            statuss = pincode.objects.filter(Village__contains = search_text)
        else:
            statuss = []

        return render(request, 'index.html', {'statuss':statuss})'''