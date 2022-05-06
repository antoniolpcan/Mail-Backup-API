from vars import router_names
from .router_config import router_imap
from BackupMail.Backup import BackupMail
#from fastapi.responses import FileResponse

@router_imap.post(router_names[1])
async def mail_backup(bup: BackupMail) -> dict:
    response = bup.get_mail()
    #name = response.get('Name_file')
    print(response)
    return response
    #return FileResponse(path = f'{ziped_dir}{name}',filename = f'{name}',media_type=f"{zip_format}")