# Type of View to Use

## Level 1: ViewSet
> https://www.django-rest-framework.org/api-guide/viewsets/
### ReadOnlyModelViewSet
```python:
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
```
### ModelViewSet
```python:
# View
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# URL
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

```python:
# views.py
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from livetest.models import LiveInfo
from livetest.serializers import LiveInfoSerializer


class LiveInfoView(ModelViewSet):
    serializer_class = LiveInfoSerializer
    queryset = LiveInfo.objects.all()
    lookup_value_regex = '\d+'

    # Extra Function / Action
    @action(methods='get', detail=False)
    def latest(self, request):
        """ Get Latest """
        live = LiveInfo.objects.latest('pk')
        serializer = self.get_serializer(live)
        return Response(serializer.data)

    @action(methods='put', detail=True)
    def change_pop(self, request, pk):
        """ Modify """ 
        live = self.get_object()
        live.bread = request.data.get('live_pop')
        live.save()
        serializer = self.get_serializer(live)
        return Response(serializer.data)

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('lives/', views.LiveInfoViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('lives/<int:pk>/', views.LiveInfoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path('lives/latest/', views.LiveInfoViewSet.as_view({
        'get': 'latest'
    })),
    path('lives/<int:pk>/change_pop/', views.LiveInfoViewSet.as_view({
        'put': 'change_pop'
    }))
]
```

### ViewSet
```python:
# views.py
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from livetest.models import LiveInfo
from livetest.serializers import LiveInfoSerializer


class LiveInfoViewSet(ViewSet):
    def list(self, request):
        """ Get All """
        lives = LiveInfo.objects.all()
        serializer = LiveInfoSerializer(lives, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Create One """
        serializer = LiveInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        """ Get One """
        try:
            live = LiveInfo.objects.get(pk=pk)
        except LiveInfo.DoesNotExist:
            raise Http404
        serializer = LiveInfoSerializer(live)
        return Response(serializer.data)

    def update(self, request, pk):
        """ Modify One """
        try:
            live = LiveInfo.objects.get(pk=pk)
        except LiveInfo.DoesNotExist:
            raise Http404
        serializer = LiveInfoSerializer(live, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        """ Delete One """
        try:
            live = LiveInfo.objects.get(pk=pk)
        except LiveInfo.DoesNotExist:
            raise Http404
        live.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# urls.py
from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^lives/$', views.LiveInfoViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    url(r'^lives/(?P<pk>\d+)/$', views.LiveInfoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
```

## Level 2: Mixed-in Generic APIView
> https://www.django-rest-framework.org/api-guide/generic-views/
```python:
# View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from livetest.models import LiveInfo
from livetest.serializers import LiveInfoSerializer


class LiveListView(ListCreateAPIView):
    queryset = LiveInfo.objects.all()
    serializer_class = LiveInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LiveDetailView(RetrieveUpdateDestroyAPIView):
    queryset = LiveInfo.objects.all()
    serializer_class = LiveInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# URL
path('users/', views.LiveListView.as_view()),
path('users/<int:pk>/', views.LiveDetailView.as_view()),
```

## Level 3: Generic APIView with Mixin
### GenericAPIView
```python:
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from livetest.models import LiveInfo
from livetest.serializers import LiveInfoSerializer


class LiveListView(GenericAPIView):

    queryset = LiveInfo.objects.all()
    serializer_class = LiveInfoSerializer

    def get(self, request):
        """ Get All """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ Create One """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LiveDetailView(GenericAPIView):

    queryset = LiveInfo.objects.all()
    serializer_class = LiveInfoSerializer
    
    def get(self, request, pk):
        """ Get One """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, pk):
        """ Modify One """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        """ Delete One """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
### Mixin
#### Example 1
```python:
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```
#### Example 2
```python:
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from livetest.models import LiveInfo
from livetest.serializers import LiveInfoSerializer


class LiveListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    GenericAPIView
    ):

    serializer_class = LiveInfoSerializer
    queryset = LiveInfo.objects.all()

    def get(self, request):
        """ Get All """
        return self.list(request)

    def post(self, request):
        """ Create One """
        return self.create(request)


class LiveDetailView(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    GenericAPIView
    ):

    serializer_class = LiveInfoSerializer
    queryset = LiveInfo.objects.all()

    def get(self, request, pk):
        """ Get One """
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """ Modify One """
        return self.update(request, pk)

    def delete(self, request, pk):
        """ Delete One """
        return self.destroy(request, pk)
```

## Level 4: APIView
### Example 1
```python:
# View
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# URL
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```
### Example 2
```python:
import json

from rest_framework.response import Response
from django.views import View
from livetest.models import LiveInfo
from livetest.serializers import LiveInfoSerializer


class LiveListView(APIView):
    def get(self, request):
        """ Get All """
        lives = LiveInfo.objects.all()
        serializer = LiveInfoSerializer(lives, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ Create One """
        json_dict = json.dumps(request.body.decode())
        serializer = LiveInfoSerializer(data=json_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LiveDetailView(APIView):
    def get(self, request, pk):
        """ Get One """
        try:
            live = LiveInfo.objects.get(pk=pk)
        except LiveInfo.DoesNotExist:
            raise Http404
        serializer = LiveInfoSerializer(live)
        return Response(serializer.data)

    def put(self, request, pk):
        """ Modify One """
        try:
            live = LiveInfo.objects.get(pk=pk)
        except LiveInfo.DoesNotExist:
            raise Http404
        json_dict = json.dumps(request.body.decode())
        serializer = LiveInfoSerializer(live, data=json_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        """ Delete One """
        try:
            live = LiveInfo.objects.get(pk=pk)
        except LiveInfo.DoesNotExist:
            raise Http404
        live.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
```

## Level 5: View (Not Used)
```python:
import json

from django.http import JsonResponse, HttpResponse
from django.views import View
from livetest.models import LiveInfo
from livetest.serializers import LiveInfoSerializer


class LiveListView(View):
    def get(self, request):
        """ Get All """
        lives = LiveInfo.objects.all()
        serializer = LiveInfoSerializer(lives, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """ Create One """
        json_dict = json.dumps(request.body.decode())
        serializer = LiveInfoSerializer(data=json_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=201)


class LiveDetailView(View):
    def get(self, request, pk):
        """ Get One """
        try:
            live = LiveInfo.objects.get(pk=pk)
        except LiveInfo.DoesNotExist:
            return HttpResponse(status=404)
        serializer = LiveInfoSerializer(live)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        """ Modify One """
        try:
            live = LiveInfo.objects.get(pk=pk)
        except LiveInfo.DoesNotExist:
            return HttpResponse(status=404)
        json_dict = json.dumps(request.body.decode())
        serializer = LiveInfoSerializer(live, data=json_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)

    def delete(self, request, pk):
        """ Delete One """
        try:
            live = LiveInfo.objects.get(pk=pk)
        except LiveInfo.DoesNotExist:
            return HttpResponse(status=404)
        live.delete()

        return HttpResponse(status=204)
```

## Level 5: Function (Not Used)
```python:
# View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# URL
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```