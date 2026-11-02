from django import forms
from .models import Producto

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=100,
        required=True
    )

    email = forms.EmailField(
        label="Correo electrónico",
        required=True
    )

    asunto = forms.CharField(
        label="Asunto",
        max_length=150,
        required=True
    )

    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea,
        required=True
    )
    telefono = forms.CharField(
    label="Teléfono",
    max_length=20,
    required=False
)

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = [
            "categoria",
            "nombre",
            "descripcion",
            "precio",
            "stock",
            "marca",
            "imagen",
        ]