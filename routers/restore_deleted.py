from vars import router_names
from .router_config import router_imap, deleted_description
from BackupMail.Backup import BackupMail

@router_imap.post(router_names[3], description = deleted_description)
def restore_deleted(bup: BackupMail) -> str:
    response = bup.send_deleted_to_email()
    return response