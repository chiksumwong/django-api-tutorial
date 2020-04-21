from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets

from f_file.models import File
from f_file.serializers import FileSerializer


class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAdminUser]


# class ImageUploadView(APIView):
#     parser_class = (FileUploadParser,)
#
#     def post(self, request, *args, **kwargs):
#
#         file_serializer = FileSerializer(data=request.data)
#
#         if file_serializer.is_valid():
#             file_serializer.save()
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
