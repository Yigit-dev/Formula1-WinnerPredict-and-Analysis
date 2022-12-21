from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("api/formula1", views.Formula1, basename = "formula1")
router.register("api/teams", views.Team, basename = "teams")
router.register("api/races", views.Races, basename = "races")
router.register("api/drivers", views.Drivers, basename = "drivers")

urlpatterns = router.urls