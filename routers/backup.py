from vars import router_names
from .router_config import router_imap
from BackupMail.Backup import BackupMail

@router_imap.post(router_names[1])
async def mail_backup(bup: BackupMail) -> dict:
    response = bup.get_mail()
    return response