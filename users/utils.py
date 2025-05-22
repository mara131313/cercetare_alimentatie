from .models import AuditLog

# face o inregistrare in tabelul AuditLog, pentru a putea genera lista in
# pe pagina audit
def log_actiune(user, actiune):
    AuditLog.objects.create(user=user, actiune=actiune)