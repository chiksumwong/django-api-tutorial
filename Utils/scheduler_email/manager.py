import logging
import json
import traceback
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.core import mail
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils import timezone

from scheduler_email.models import EmailTask, EmailCheckExpiredTime

logger = logging.getLogger('system.email')


def add_confirm_email_task(user_id):
    try:
        user = User.objects.get(pk=user_id)
        e_to = [user.email]
        e_cc = ['samwongdev20@gmail.com']
        data = {
            "subject": f"[Application]: Confirmation",
            "from": settings.EMAIL_HOST_USER,
            "to": e_to,
            "cc": e_cc,
            "template": "confirm_letter.html",
            "content": {
                "username": user.username,
            }
        }

        EmailTask.objects.create(params=json.dumps(data))
        logger.info(f'Added confirmation email: {user_id}')

    except User.DoesNotExist:
        logger.error(f'\nEMAIL ERROR: user not found: {user_id}')
    except Exception as e:
        logger.error(f'\nEMAIL ERROR: add_email_task_2 Error\n{e}\n{traceback.format_exc()}')


# Function
def run_email_task_send():
    try:
        RETRY_AVAILABLE = 1
        last_hour_date_time = timezone.now() - timedelta(minutes=15)

        tasks = EmailTask.objects \
            .filter(Q(status=EmailTask.Status.PENDING) |
                    (Q(status=EmailTask.Status.SENDING) & Q(start_at__lte=last_hour_date_time)) & Q(count__lte=RETRY_AVAILABLE) |
                    (Q(status=EmailTask.Status.FAIL) & Q(start_at__lte=last_hour_date_time)) & Q(count__lte=RETRY_AVAILABLE)) \
            .order_by('created_at') \
            .only('id')

        if len(tasks) > 0:
            connection = mail.get_connection()
            connection.open()

            task_len = len(tasks)
            task_count = 1
            logger.info(f'===== Start To Send Email: {task_len} =====')

            for task in tasks:
                logger.info(f'Email Sending: {task_count} / {task_len}')
                ex_task = EmailTask.objects.get(id=task.id)
                if ex_task.status != EmailTask.Status.COMPLETED:
                    ex_task.status = EmailTask.Status.SENDING
                    ex_task.start_at = timezone.now()
                    ex_task.count = ex_task.count + 1
                    ex_task.save()

                    result = send_email_html(ex_task.params, connection)

                    if result == 'ok':
                        ex_task.status = EmailTask.Status.COMPLETED
                    else:
                        ex_task.status = EmailTask.Status.FAIL

                    if ex_task.result is not None:
                        ex_task.result = '\n'.join(
                            [str(ex_task.result), f'{timezone.now()}, Count {ex_task.count}: {result}'])
                    else:
                        ex_task.result = f'{timezone.now()}, Count {ex_task.count}: {result}'
                    ex_task.save()
                task_count += 1

            logger.info('===== End To Send Email =====')
            connection.close()
    except EmailTask.DoesNotExist:
        logger.error(f'\nEMAIL ERROR: run_send_email_task Error\nEmailTask Detail Does Not Exist')
    except Exception as e:
        logger.error(f'\nEMAIL ERROR: run_send_email_task Error\n{e}\n{traceback.format_exc()}')


def send_email_html(e_obj, connection):
    try:
        obj_js = json.loads(e_obj)
        e_subject = obj_js['subject']
        e_from = obj_js['from']
        e_to = obj_js['to']
        e_cc = obj_js['cc']
        e_content = render_to_string(
            obj_js['template'],
            obj_js['content']
        )

        email = EmailMultiAlternatives(
            subject=e_subject,
            from_email=e_from,
            to=e_to,
            cc=e_cc,
            connection=connection
        )
        email.attach_alternative(e_content, 'text/html')
        email.send()

        logger.info('Email Sent')
        return 'ok'

    except BadHeaderError as e:
        connection.close()
        logger.error(f'\nEMAIL ERROR: Bad Header Error\n{traceback.format_exc()}')
        return f'\nEMAIL ERROR: Bad Header Error\n{e}'
    except Exception as e:
        connection.close()
        logger.error(f'\nEMAIL ERROR: Send Email Error\n{traceback.format_exc()}')
        return f'\nEMAIL ERROR: Send Email Error\n{e}'