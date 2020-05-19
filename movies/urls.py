from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from movies.views import ActorsViewSet, MoviesViewSet

router = DefaultRouter(trailing_slash=False)
router.register(
    r'api/movies',
    MoviesViewSet,
    basename='movies'
)
router.register(
    r'api/actors',
    ActorsViewSet,
    basename='actors'
)

patterns = router.urls
