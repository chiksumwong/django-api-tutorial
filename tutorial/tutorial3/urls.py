from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tutorial3 import views_mixins

urlpatterns = [
    path('snippets/', views_mixins.SnippetList.as_view()),
    path('snippets/<int:pk>/', views_mixins.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)