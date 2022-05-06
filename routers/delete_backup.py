from vars import router_names
from .router_config import router_imap, delete_description
from BackupMail.Backup import BackupMail

@router_imap.delete(router_names[4], description = delete_description)
async def delete_backup(bup: BackupMail) -> dict:
    if bup.login_email():
        return bup.remove_dir_and_files()