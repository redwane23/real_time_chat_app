from django.apps import AppConfig


class AuthonticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authontication'
    def ready(self):
        import authontication.signals  
