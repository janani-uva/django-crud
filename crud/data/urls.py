from django.urls import path
from .views import studentListCreate, studentRetrieveUpdateDestroy


urlpatterns = [
    path('student/',studentListCreate.as_view(), name='student-list-create'),
    path('student/<int:pk>/', studentRetrieveUpdateDestroy.as_view(), name='student-detail')
]
