from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("api/todo", views.TODOViewSet, basename = "todo")

urlpatterns = router.urls