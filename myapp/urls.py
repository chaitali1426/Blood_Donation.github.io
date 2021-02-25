from django.contrib import admin
from django.urls import path
from .import views as v
#from tempapp import views
urlpatterns = [
    
    path('', v.home),
    path('donor_registration',v.donorregdisplay),
    path('donors', v.donorregdisplay, name='dregdisplay'),
    path('home',v.home),

    path('about',v.about),
   
    path('blood_search',v.searchdisplay, name='searchsite1'),
    path('donorlist/',v.searchdisplay, name='donorlistsite'),
    path('donorlist/donorlistdetail/<email>/', v.donorlistdetail, name='donorlistdetailsite'),
    path('contact_us',v.contact),
     

]
