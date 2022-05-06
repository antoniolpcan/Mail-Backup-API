from .router_config import router
from vars import router_names
from BackupMail.Backup import BackupMail

@router.post(router_names[0])
def login(bup: BackupMail) -> str:
    login_info = bup.login_email()
    return login_info