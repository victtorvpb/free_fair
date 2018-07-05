from django.urls import path


from .apiviews import ItsAliveView

app_name = 'core'

urlpatterns = [path('its_alive', ItsAliveView.as_view(), name="itsalive")]
