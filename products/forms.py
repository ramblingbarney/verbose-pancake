from django import forms
from django.conf import settings
from .models import Product, ProductArea
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat


class NewProductForm(forms.ModelForm):
    '''
    Form used to create a new product (feature/issue)
    '''

    class Meta:
        model = Product
        fields = [
            'name', 'description', 'price', 'product_area',
            'product_need', 'product_complexity', 'status', 'product_type',
            'image', 'product_document']

    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop('id', None)
        super(NewProductForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(NewProductForm, self).clean()
        if 'product_area' in self._errors:
            del self._errors['product_area']
        return self.cleaned_data

    def clean_name(self, **kwargs):
        name = self.cleaned_data.get('name')
        pk = self.instance.id

        if pk is None:
            if Product.objects.filter(name__iexact=name):
                raise forms.ValidationError(u'Name must be unique')
        elif pk:
            if Product.objects.filter(name__iexact=name).filter(id=pk):
                return name
            else:
                if Product.objects.filter(name__iexact=name):
                    raise forms.ValidationError(u'Name must be unique')
        return name

    def clean_image(self):

        image = self.cleaned_data['image']
        if image is None:
            return 'images/image_placeholder.jpeg'
        else:
            return image

    def clean_product_document(self):
        '''
        Function taken from https://stackoverflow.com/questions/4853581/django-get-uploaded-file-type-mimetype
        '''

        file = self.cleaned_data['product_document']
        if file is None or isinstance(file, str):
            return file
        else:
            try:
                if file:
                    file_type = file.content_type.split('/')[0]

                    if len(file.name.split('.')) == 1:
                        raise forms.ValidationError(u'File type is not supported')

                    if file_type in settings.TASK_UPLOAD_FILE_TYPES:
                        if file.size > int(settings.TASK_UPLOAD_FILE_MAX_SIZE):
                            raise forms.ValidationError(('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.TASK_UPLOAD_FILE_MAX_SIZE), filesizeformat(file.size)))
                    else:
                        raise forms.ValidationError(('File type is not supported'))
            except AttributeError:
                pass

        return file


class NewProductAreaForm(forms.ModelForm):
    """
    Form used to create a new product area
    """

    class Meta:
        model = ProductArea
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if ProductArea.objects.filter(name__iexact=name):
            raise forms.ValidationError(u'Name must be unique')
        return name

    # TODO: TEsts, product area, create, duplicaes
