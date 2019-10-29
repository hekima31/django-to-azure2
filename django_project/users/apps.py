from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

#This is necessary to allow the built-in signals function to work
    def ready(self):
        import users.signals
