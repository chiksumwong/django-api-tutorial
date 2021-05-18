# Serializer & View & Router
> https://kknews.cc/code/xgyy82q.html

## Serializer
1. serializers.Serializer
```python:
class LiveInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) 
    live_id = serializers.IntegerField()
    live_streamer = serializers.CharField(max_length=20, required=False)
    live_title = serializers.CharField(max_length=30)
    live_pop = serializers.IntegerField(default=0, required=False)
    live_content = serializers.CharField(default='未設定', max_length=20, required=False)
    is_delete = serializers.BooleanField(default=False, required=False)
```
- write_only：True, Deserialization
- read_only：True, Serialization
- required：True, Deserialization
- default：default value
- max_length & min_length：max and min length
- max_value & min_value：max and min number

2. Serializer - Sub List
   1. PrimaryKeyRelateField
    ```python:
    Ltype = serializers.PrimaryKeyRelatedField(read_only=True)

    # OR

    Ltype = serializers.PrimaryKeyRelatedField(queryset=LiveInfo.objects.all())
    ```
   2. Serializer in Serializer (Best)
    ```python:
    Ltype = LiveInfoSerializer()
    ```
   3. Get sub return \_\_str\_\_
    ```python:
    Ltype = serializers.StringRelatedField(many=True)
    ```

3. Serializer's Validation (validate__field_name)

4. serializer.ModelSerializer (If target of serializer is a model)
   - Base on model field, auto generate the serializer/validation field
   - Provide default create() and update()
    ```python:
    class LiveInfoSerializer(serializers.ModelSerializer): 
        class Meta: model = LiveInfo 
        fields = '__all__' 
        # fields = ('id', 'title', ...)

        # exclude some field 
        exclude = ['is_delete'] 
        
        # extra field
        extra_kwargs = { 
            # 'live_title': {'validators': [live_name]},
            'live_streamer': {'required': False},
            'live_pop': {'min_value': 0, 'required': False}, 
            }
    ```

## Views
1. Level 1 (not use serializer)
- Class View
- Access Database
- JsonResponse (serializer)
 ```python:
 class LiveListView(View): 
     def get(self, request):

        lives = LiveInfo.objects.all() 
        lives_list = [] 

        for live in lives: 
            lives_list.append({ 
                'live_id': live.live_id,
                'live_streamer': live.live_streamer,
                'live_title': live.live_title,
                'live_pop': live.live_pop,
                'live_content': live.live_content
                })

        return JsonResponse(lives_list, safe=False)

```

2. Level 2 (use serializer)
```python:
class LiveDetailView(View): 
    def get(self, request, pk): 
        try: 
            live = LiveInfo.objects.get(pk=pk) 
        except LiveInfo.DoesNotExist: 
            return HttpResponse(status=404)

        serializer = LiveInfoSerializer(live)

        return JsonResponse(serializer.data)  # dict

class LiveListView(View): 
    def get(self, request): 
        lives = LiveInfo.objects.all() 
        serializer = LiveInfoSerializer(lives, many=True)  # Multiple
        return JsonResponse(serializer.data, safe=False)
```

3. APIView
   - request.data (for post, e.g. request.data.get('key'))
   - request.query_params (for get, e.g. request.query_params.get('key'))
   - Response Object (base on Accept of Header from client, it will tell server which are client able to read) (e.g. return Response(result, status=status.HTTP_200_OK))
   - Handle Exception (return to client)
   - Auth / Permission / Throttle

4. GenericAPIView, extend APIView
   - Extend APIView
   - Add Handle Serializer (serializer_class, get_serializer_class, get_serializer)
   - Add Handle Model Query (get_queryset, get_object)
   - Filtering and Pagination

5. 5 type Mixin
   1. ListModelMixin
   2. CreateModelMixin
   3. RetrieveModelMixin
   4. UpdateModelMixin
   5. DestroyModelMixin

6. 9 type Sub APIView, extend GenericAPIView and related Mixin
   1. ListAPIView
   2. CreateAPIView
   3. RetrieveAPIView
   4. UpdateAPIView
   5. DestroyAPIView
   6. ListCreateAPIView
   7. RetrieveUpdateAPIView
   8. RetrieveDestroyAPIView
   9. RetrieveUpdateDestroyAPIView

7. ViewSet
   1. GenericViewSet
   2. ModelViewSet
   3. ReadOnlyModelViewSet


## Router
1. Simple Router
2. Default Router

The difference between DefaultRouter and SimpleRouter generates an additional root path (/) configuration item, and each configuration item address can follow .json and return json data directly.

```python:
from rest_framework.routers 
import DefaultRouter 
from livetest import views 

urlpatterns = []

router = DefaultRouter() 
router.register('lives', views.LiveInfoView, base_name='live')

urlpatterns += router.urls
```

## Other Function
The DRF framework has other functions: authentication, permissions, current limiting, filtering, sorting, paging, and exception handling mechanisms.


## Example 1 (View with Serializer)
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

## Example 2 (Generic API View)
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

## Example 3 (Mixin)
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


## Example 4 (Sub APIView & Mixin)
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

## Example 5 (ViewSet)
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

## Example 6 (ModelViewSet)
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

## DRF View Architecture
<kbd>
<img src='images/DRF_View.png' width="800" alt='DRF View'>
</kbd>