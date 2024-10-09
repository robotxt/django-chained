from rest_framework import routers
from blockchain import views


router = routers.DefaultRouter()
router.register("events", views.EventDataApiEndpoint, basename="event-api")
