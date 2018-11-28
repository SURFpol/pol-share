from django.urls import reverse
from django import forms

from ims.models import CommonCartridge


class CommonCartridgeShared(CommonCartridge):

    def get_absolute_url(self):
        return reverse('share:common-cartridge-upload-success', kwargs={"pk": self.id})

    class Meta:
        proxy = True


class CommonCartridgeSharedForm(forms.ModelForm):

    # TODO: check necessity of a form.clean
    # def clean(self):
    #     self.instance.clean()  # TODO: is this necessary?
    #     # TODO: check metadata
    #     super().clean()

    class Meta:
        model = CommonCartridgeShared
        fields = ['file']
