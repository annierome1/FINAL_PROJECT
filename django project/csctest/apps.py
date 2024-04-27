#######################
#####
##### Apps code that allows app to exist
#####
#######################

#imports needed functions
from django.apps import AppConfig

#creates class for app
class CsctestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'csctest'
