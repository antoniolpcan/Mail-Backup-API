from vars import router_names
from .router_config import router_imap
from BackupMail.Backup import BackupMail

@router_imap.post(router_names[0])
def login(bup: BackupMail) -> str:
    login_info = bup.login_email()
    return login_info