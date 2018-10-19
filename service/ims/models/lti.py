import uuid
from oauthlib.common import generate_token

from django.db import models


class LTIPrivacyLevels(object):
    ANONYMOUS = 'anonymous'
    EMAIL_ONLY = 'email_only'
    NAME_ONLY = 'name_only'
    PUBLIC = 'public'


PRIVACY_LEVEL_CHOICES = tuple([
    (value, value) for attr, value in sorted(LTIPrivacyLevels.__dict__.items()) if not attr.startswith("_")
])


VIEW_CHOICES = (
    ('share:common-cartridge-upload', 'Common Cartridge upload'),
)


class LTIApp(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True)
    view = models.CharField(max_length=50, choices=VIEW_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    title = models.CharField(max_length=128)
    description = models.TextField()
    privacy_level = models.CharField(max_length=50, choices=PRIVACY_LEVEL_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'LTI app'
        verbose_name_plural = 'LTI apps'


class LTICredentials(models.Model):

    client_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_secret = models.CharField(max_length=30, default=generate_token, editable=False)
    app = models.ForeignKey(LTIApp)
    organization = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.client_key)

    class Meta:
        verbose_name = 'LTI credentials'
        verbose_name_plural = 'LTI credentials'
