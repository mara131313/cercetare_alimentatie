from .models import AuditLog

def log_actiune(user, actiune):
    AuditLog.objects.create(user=user, actiune=actiune)
