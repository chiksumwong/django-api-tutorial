from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tutorial4 import views as t4view
from tutorial5 import views as t5view

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', t5view.api_root),
    path('snippets/<int:pk>/highlight/', t5view.SnippetHighlight.as_view()),

    # snippets list and detail
    path('snippets/', t4view.SnippetList.as_view()),
    path('snippets/<int:pk>/', t4view.SnippetDetail.as_view()),

    # user list and detail
    path('users/', t4view.UserList.as_view()),
    path('users/<int:pk>/', t4view.UserDetail.as_view())
])
