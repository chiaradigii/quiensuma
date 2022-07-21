from django import forms

from .models import Jugador

class SingUpForm(forms.ModelForm):

    class Meta:
        model = Jugador
        fields =  ('__all__')
        widgets = {

            'categoria' : forms.CheckboxSelectMultiple()
        }
# class SingUpForm(UserCreationForm):
#     correo = forms.EmailField()
#     sexo = forms.CharField()
#     localidad = forms.CharField()
#     provincia = forms.CharField()
#     imagen=forms.ImageField()
#     nombre=forms.CharField()
#     apellido=forms.CharField()
#     fecha_nacimiento = forms.DateField(help_text='Formato: YYYY-MM-DD')
#     descripcion = RichTextField()
   
#     class Meta:
#         model = User
#         fields =  ("username", "password1", "password2",'correo','sexo','localidad','apellido','nombre','provincia','imagen','fecha_nacimiento','categoria','descripcion')
#         widgets = {

#             'categoria' : forms.CheckboxSelectMultiple()
#         }

#     def save(self,commit=True):
#         jugador = super(SingUpForm,self).save(commit=False)
#         jugador.correo = self.cleaned_data['correo']
#         jugador.sexo =self.cleaned_data['sexo']
#         jugador.localidad = self.cleaned_data['localidad']
#         jugador.apellido = self.cleaned_data['apellido']
#         jugador.nombre = self.cleaned_data['nombre']
#         jugador.provincia = self.cleaned_data['provincia']
#         jugador.imagen = self.cleaned_data['foto de perfil'] 
#         jugador.fecha_nacimiento = self.cleaned_data['fecha de nacimiento']
#         jugador.descripcion=self.cleaned_data['Describa brevemente su esilo de juego']
#         if commit:
#             jugador.save()
#         return jugador
