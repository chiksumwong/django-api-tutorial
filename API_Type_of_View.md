# Type of View to Use

## Level 1: ViewSet
### ModelViewSet
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

    # Extra Function
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
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^lives/$', views.LiveInfoViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    url(r'^lives/(?P<pk>\d+)/$', views.LiveInfoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    url(r'^lives/latest/$', views.LiveInfoViewSet.as_view({
        'get': 'latest'
    })),
    url(r'^lives/(?P<pk>\d+)/change_pop/$', views.LiveInfoViewSet.as_view({
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
```python:
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from livetest.models import LiveInfo
from livetest.serializers import LiveInfoSerializer


class LiveListView(ListCreateAPIView):
    serializer_class = LiveInfoSerializer
    queryset = LiveInfo.objects.all()


class LiveDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = LiveInfoSerializer
    queryset = LiveInfo.objects.all()
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
    serializer_class = LiveInfoSerializer
    queryset = LiveInfo.objects.all()

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
    serializer_class = LiveInfoSerializer
    queryset = LiveInfo.objects.all()

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

## Level 5: View
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