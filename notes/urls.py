from rest_framework.routers import DefaultRouter

from notes.views import NoteViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet)
urlpatterns = router.urls
