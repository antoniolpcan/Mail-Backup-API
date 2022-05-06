from vars import router_names
from .router_config import router_imap
from BackupMail.Backup import BackupMail

@router_imap.post(router_names[3])
def deleted_to_email(bup: BackupMail) -> str:
    response = bup.send_deleted_to_email()
    return response