from vars import router_names
from .router_config import router_imap
from BackupMail.Backup import BackupMail

@router_imap.post(router_names[2])
def to_email(bup: BackupMail):
    response = bup.send_to_email()
    return response
