from f_system_log.models import AccessLog, AuditLog, SyncLog


def save_access_log(message):
    log = AccessLog(message=message)
    log.save()


def save_audit_log(message):
    log = AuditLog(message=message)
    log.save()


def save_sync_log(message):
    log = SyncLog(message=message)
    log.save()