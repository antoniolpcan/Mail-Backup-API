from functions.__init__ import get_mail
from fastapi import Depends
from fastapi.responses import FileResponse
from .router_config import router

@router.post('/')
async def mail_backup(name = Depends(get_mail)):
    return FileResponse(path = f'imap/imap_compact/{name}',filename = f'{name}',media_type="zip")