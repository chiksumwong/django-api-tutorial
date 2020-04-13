from rest_framework import serializers

from f_file.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = "__all__"
