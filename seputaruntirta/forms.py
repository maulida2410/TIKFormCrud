from django.forms import ModelForm
from django import forms
from seputaruntirta.models import Dosen, Staf, Mahasiswa

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'

        widgets = {
            'NIP' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggallahir': forms.TextInput({'class':'form-control'}),
            'photo': forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
        }

class FormStaf(ModelForm):
    class Meta:
        model = Staf
        fields = '__all__'

        widgets = {
            'NIP' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggallahir': forms.TextInput({'class':'form-control'}),
            'photo': forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
        }

class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'

        widgets = {
            'NIP' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggallahir': forms.TextInput({'class':'form-control'}),
            'photo': forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
        }