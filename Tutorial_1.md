# Tutorial 1 - Serializer

## Serializer Introduction
- Python Object --> JSON (Render)
- JSON --> Python Object (Parser)

### Using "Serializer" serializer (Basic Type)
- defines the fields that get serialized/deserialized
- able to set "VALIDATION" (such as required, max_length, default)
- field can control the how the browsable API should be displayed 

### Using "ModelSerializers" (Extend Serializer)
- more concise
- automatically determined set of fields
- default implementations for the "create()" and "update()" methods

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

## Working ModelSerializer
```python
from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))  # define a serializer which have what fields..., like define a Django's Form Object
# SnippetSerializer():
#    id = IntegerField(label='ID', read_only=True)
#    title = CharField(allow_blank=True, max_length=100, required=False)
#    code = CharField(style={'base_template': 'textarea.html'})
#    linenos = BooleanField(required=False)
#    language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'), ('ada', 'Ada')...
#    style = ChoiceField(choices=[('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful')...
```