from django.urls import include, path

from v1.user.urls import user_routes

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("users/", include(user_routes.urls)),
]