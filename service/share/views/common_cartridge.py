from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView


from ims.models import CommonCartridge, CommonCartridgeForm


class CommonCartridgeUploadView(CreateView):
    model = CommonCartridge
    template_name = 'share/common_cartridge/upload.html'
    form_class = CommonCartridgeForm


class CommonCartridgeDetailView(DetailView):
    model = CommonCartridge
    template_name = 'share/common_cartridge/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["metadata"] = self.object.get_metadata()
        return context
