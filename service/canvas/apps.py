from django.apps import AppConfig
from datagrowth.configuration.types import register_defaults

from canvas.constants import CanvasVisibility


class CanvasConfig(AppConfig):
    name = 'canvas'

    def ready(self):
        register_defaults('ims', {
            'canvas_course_navigation_visibility': CanvasVisibility.ADMINS
        })
