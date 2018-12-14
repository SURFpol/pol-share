from django.apps import AppConfig
from dgconfig.types import register_config_defaults

from canvas.constants import CanvasVisibility


class CanvasConfig(AppConfig):
    name = 'canvas'

    def ready(self):
        register_config_defaults('ims', {
            'canvas_course_navigation_visibility': CanvasVisibility.ADMINS
        })
