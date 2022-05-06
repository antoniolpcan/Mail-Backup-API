from vars import router_names
from .router_config import router_imap,login_description
from BackupMail.Backup import BackupMail

@router_imap.post(router_names[0], description = login_description)
def login(bup: BackupMail) -> str:
    login_info = bup.login_email()
    return login_info