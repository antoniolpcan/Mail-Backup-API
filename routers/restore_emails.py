from vars import router_names
from .router_config import router_imap, to_email_description
from BackupMail.Backup import BackupMail

@router_imap.post(router_names[2], description = to_email_description)
def restore_emails(bup: BackupMail):
    response = bup.send_to_email()
    return response
