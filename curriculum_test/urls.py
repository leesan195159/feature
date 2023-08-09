from django.urls import path, include

urlpatterns = [
    path('curriculum', include('curriculum.urls'))
]
