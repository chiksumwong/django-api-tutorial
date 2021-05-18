# Serializer

## Django REST Framework Introduction
- Provide Serializer
- MiXin Extend
- Simplify View Code
- Increase the speed of API developing

## Serializer Introduction
- Python Object --> JSON (Render)
- JSON --> Python Object (Parser)
- Validation

## Type of Serializer
### "Serializer" (Basic Type, Extend BaseSerializer)
- defines the fields that get serialized/deserialized
- able to set "VALIDATION" (such as required, max_length, default)
- field can control the how the browsable API should be displayed 

### "ListSerializer" (Extend BaseSerializer)
- serialize multiple model
- will be instantiated if serializer set "many=True"

### "ModelSerializer" (Extend Serializer)
- more concise
- automatically determined set of fields
- default implementations for the "create()" and "update()" methods

### "HyperlinkedModelSerializer" (Extend ModelSerializer)
- add a field "url"
- able to click the url to redirect that record


## Working with Serializer
## Serialization - "Model" to "JSON"
```python
from tutorial1.models import Snippet
from tutorial1.serializers import SnippetSerializer

from rest_framework.renderers import JSONRenderer
```

```python
snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()
```

to Python native datatypes
```python
serializer = SnippetSerializer(snippet)
serializer.data
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
```

to Json
```python
content = JSONRenderer().render(serializer.data)
content
# b'{"id": 2, "title": "", "code": "print(\\"hello, world\\")\\n", "linenos": false, "language": "python", "style": "friendly"}'
```
## Deserialization "JSON" to "Model"
Parse a stream into Python native datatypes
```python
import io
from rest_framework.parsers import JSONParser

stream = io.BytesIO(content)
data = JSONParser().parse(stream)
```
Native datatypes into an object instance
```python
serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object> (model instance)
```
