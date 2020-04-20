from django.contrib.auth.models import User
from tutorial4.models import SnippetAuth
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=SnippetAuth.objects.all())  # return all PK

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']  # 'snippets' is above fields which just define


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Cannot update when deserialized

    class Meta:
        model = SnippetAuth
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
