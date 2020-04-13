# Tutorial 1: Serialization
- Model to JSON
- JSON to Model

## Type
- ModelSerializer
- HyperlinkedModelSerializer

# Tutorial 2: Request and Responses
## Request, Response, Status
- Using DRF's `Request` replace Django's "request.POST"
- Using DRF's `Response` replace Django http's "HttpResponse" and "JsonResponse"
- Using DRF's `Status` object

p.s.
- `application/x-www-form-urlencoded` (Normal Way to Submit)
- `multipart/form-data` (Normal Way to Submit file / multi file)
## Wrapping API views
- `@api_view` for function based views
- `APIView` for class-base views

## Format Suffixes API for "Browsable API" (options)
- will return the api with different format which define by request header set `Accept`, e.g. "application/json", "text/html"
- able to return a web-browsable API ("text/html" format)
1. set "format=None" in view's function
2. import "format_suffix_patterns" in app's urls

# Tutorial 3: Class-base Views
## Class-base Views
- allow us to easily compose reusable bits of behavior by using "Mixins"

## Mixins (Python Multi Inheritance)
- System will provide the basic CURD behavior
- But we can rewrite the behavior which we want by Mixinsing the code that we write and system default
- reduce the code which need to write

## Generics
- a set of already mixed-in generic views that DRF provides

`(Tutorial 4-6, Add Authentication and Permission)`

# Tutorial 4: Authentication & Permissions
### Aims
- Code snippets are always associated with a creator.
- Only authenticated users may create snippets.
- Only the creator of a snippet may update or delete it.
- Unauthenticated requests should have full read-only access.

### Associating DRF Auth's `User Model` with `Other Model`



# Tutorial 5: Relationships & hyperlinked APIs
- add url field, then able to redirect other record


# Tutorial 6: ViewSets & Routers
- viewset automatically provides `list` and `detail` actions.

## Biding ViewSets to URLs Explicitly
```python
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# Route
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
```

## OR - Just Let Router Do Above
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
```