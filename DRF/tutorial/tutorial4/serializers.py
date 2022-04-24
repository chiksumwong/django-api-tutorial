from django.contrib.auth import get_user_model
from tutorial4.models import SnippetAuth
from rest_framework import serializers

User = get_user_model()


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
