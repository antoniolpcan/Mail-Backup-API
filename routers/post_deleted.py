from vars import *
from .router_config import router
from BackupMail.Backup import BackupMail

@router.post(router_names[3])
def deleted_to_email(bup: BackupMail) -> str:
    response = bup.send_deleted_to_email()
    return response