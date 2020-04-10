import django

django.setup()

from tutorial1.models import Snippet
from tutorial1.serializers import SnippetSerializer

import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

if __name__ == '__main__':
    # Serialization - "Model" to "JSON"
    print('Serialization - "Model" to "JSON"')
    print()

    snippet = Snippet(code='foo = "bar"\n')
    print('model:', snippet)
    print(type(snippet))
    print()

    serializer = SnippetSerializer(snippet)
    print('serializer field setting, input a Object:')
    print(serializer)
    print(type(serializer))
    print()

    print('Serializer\'s data, dict like but not dict:')
    print(serializer.data)
    print(type(serializer.data))
    print()

    print('JSON, b means "Bytes", is python3 data format:')
    json = JSONRenderer().render(serializer.data)
    print(json)
    print(type(json))
    print()

    # Deserialization - "JSON" to "Model"
    print('Deserialization - "JSON" to "Model"')
    print()

    print('Steaming:')
    stream = io.BytesIO(json)
    print(stream)
    print(type(stream))
    print()

    print('Data Type - Dick:')
    data = JSONParser().parse(stream)
    print(data)
    print(type(data))
    print()

    print('deserializer:')
    serializer = SnippetSerializer(data=data)
    print(serializer)
    print(type(serializer))
    print()

    print('validation:')
    print(serializer.is_valid())  # True
    print(type(serializer.is_valid()))
    print()

    print('serializer\'s validated data, still not the model object:')
    print(serializer.validated_data)
    print(type(serializer.validated_data))

    print('If want to get the model object, need the create() or update() method which implement in serializer')
