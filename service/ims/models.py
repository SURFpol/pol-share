import os
from zipfile import ZipFile

from django.db import models
from django import forms
from django.core.exceptions import ValidationError


class CommonCartridge(models.Model):

    file = models.FileField()
    manifest = models.TextField(blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        tail, head = os.path.split(self.file.name)
        return head


class CommonCartridgeForm(forms.ModelForm):

    def clean(self):
        cartridge = ZipFile(self.files['file'])
        try:
            self.instance.manifest = str(cartridge.read('imsmanifest.xml'), encoding='utf-8')
        except KeyError:
            raise ValidationError('The common cartridge should contain a manifest file')
        super().clean()

    class Meta:
        model = CommonCartridge
        fields = ['file']
