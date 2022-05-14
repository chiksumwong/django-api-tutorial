import logging

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from scheduler_email.manager import run_email_task_send, add_confirm_email_task

logger = logging.getLogger('system.email')


# For Testing
@api_view(['GET'])
@permission_classes([AllowAny])
def test_add_confirm_email_task(request):
    add_confirm_email_task('1')
    return Response({'Message': 'ok'}, status=status.HTTP_200_OK)


# For Testing
@api_view(['GET'])
@permission_classes([AllowAny])
def test_run_send_email_task(request):
    run_email_task_send()
    return Response({'Message': 'ok'}, status=status.HTTP_200_OK)
