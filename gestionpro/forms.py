from django import forms
from .models import Servicio, Producto 
from django.utils.safestring import mark_safe
import base64

class ImagenBinariaForm(forms.ModelForm):
    imagen_file = forms.ImageField(required=False, label="Imagen")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.imagen:
            imagen_preview = base64.b64encode(self.instance.imagen).decode()
            self.fields['imagen_file'].help_text = mark_safe(
                f'<br><strong>Vista previa:</strong><br>'
                f'<img src="data:image/jpeg;base64,{imagen_preview}" '
                f'style="max-height: 200px;">'
            )

    class Meta:
        exclude = ['imagen']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('imagen_file'):
            instance.imagen = self.cleaned_data['imagen_file'].read()
        if commit:
            instance.save()
        return instance

class ServicioForm(ImagenBinariaForm):
    class Meta(ImagenBinariaForm.Meta):
        model = Servicio

class ProductoForm(ImagenBinariaForm):
    class Meta(ImagenBinariaForm.Meta):
        model = Producto
