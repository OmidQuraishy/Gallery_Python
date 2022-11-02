from django import forms

from galleryapp.models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('name','image','description','author')
        labels  = {
        'name':'', 
        'image':'',
        'description':'',


        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام'}),
            'image':forms.FileInput(attrs={'class':'form-control ', 'placeholder':'نام'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'نام'}),
            'author':forms.TextInput(attrs={'class':'form-control', 'value':'','id':'userid','type':'hidden','placeholder':'نام'}),
            
        }


