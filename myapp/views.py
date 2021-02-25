from django.shortcuts import render,redirect
from .forms import DonorRegistration,DonorSearch
from .models import DonorList

def home(request):
    return render(request,'base.html')
#Donnor forms display
'''



'''
def donorregdisplay(request):
    forms = DonorRegistration()
    if request.method == 'POST':
        forms = DonorRegistration(request.POST)
        if forms.is_valid():
            forms.save()

            context_details ={
                'forms' : forms
            }
            #After donor registation donor details display
            return render(request, 'donor_reg_s.html', context_details)

        



    context = {
                'forms' : forms,
            }


    return render(request, 'donor_reg.html', context)



def searchdisplay(request):
    search_forms = DonorSearch()
    
    if request.method == 'POST':
        search_forms = DonorSearch(request.POST)
        if search_forms.is_valid():
            blood_group = search_forms.cleaned_data['select_blood_group']
            location = search_forms.cleaned_data['select_location']
            donor_filter = DonorList.objects.filter(blood_group=blood_group, home_address__icontains=location)
            context = {
                'donor_filter' : donor_filter
            }
            return render(request, 'donor_list.html', context)



    context = {
        'forms_search' : search_forms,
        
    }
    return render(request, 'blood_search.html' ,context)

def donorlistdetail(request, email):
    email = email
    detail = DonorList()
    detail = DonorList.objects.get(email=email)
    context = {
        'details' : detail
    }
    return render(request, 'donor_l_d.html', context)

def contact(request):
    return render(request,'contct_us.html')

def about(request):
    return render(request,'about.html')