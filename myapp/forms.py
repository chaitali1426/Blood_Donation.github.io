from django import forms
from django.forms import ModelForm
from .models import DonorList
    
    
#Donor registrarion forms create
class DonorRegistration(ModelForm):
    class Meta:
        model = DonorList
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'blood_group' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'home_address' : forms.Textarea(attrs={'class':'form-control', 'required':'True'}),
            'last_donate_date' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'any_diseases' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'allergies' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'cardiac' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'bleeding_disorders' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'hbsAg_hcv_hIV' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            
        }
        




class DonorSearch(forms.Form):
    blood_group_s_choice = (
        ("empty" , "Select blood group"),
        ("a+" , "A+"),
        ("a-" , "A-"),
        ("b+" , "B+"),
        ("b-" , "B-"),
        ("o+" , "O+"),
        ("o-" , "O-"),
        ("ab+" , "AB+"),
        ("ab-" , "AB-"),
        ("bombay_blood",'BOMBAY BLOOD'),
    )
    select_blood_group = forms.ChoiceField(
        choices=blood_group_s_choice,
        widget=forms.Select(
            attrs={'class':'form-control',
            'required':'True',
            },
            ),
    )

    select_location = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control',
            'required':'True', 
            'placeholder':'Enter your City Or Location'
            }
        ),
    )
    


