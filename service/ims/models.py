import os
from django.db import models


class CommonCartridge(models.Model):

    file = models.FileField()
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        tail, head = os.path.split(self.file.name)
        return head
