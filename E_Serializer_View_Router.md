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
- write_only：為True，字段只在反序列化時使用
- read_only：為True，字段只在序列化時使用
- required：為True，如果字段在反序列化時使用，該字段必傳傳入
- default：設置序列化和反序列化操作時的默認值
- max_length和min_length：設置字符串的最大長度和最小長度
- max_value和min_value：設置數字的最大值和最小值

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

3. APIVIew
- request.data
- request.query_params
- Response Object (base on Accept of Header from client, it will tell server which are client able to read)
- Handle Exception (return to client)
- Auth / Permission / Throttle
- Example
   1. GenericAPIView
   2. ListAPIView
   3. CreateAPIView
   4. etc...

4. Mixin
   1. ListModelMixin
   2. CreateModelMixin
   3. RetrieveModelMixin
   4. UpdateModelMixin
   5. DestroyModelMixin

5. ViewSet
   1. GenericViewSet
   2. ModelViewSet
   3. ReadOnlyModelViewSet
   
## Router
1. Simple Router
2. Default Router

DefaultRouter和SimpleRouter的區別多生成一個根路徑(/)配置項，並且每個配置項地址後都可以跟上.json，直接返回json數據。

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
DRF框架還有其他功能：認證、權限、限流、過濾、排序、分頁和異常處理機制。