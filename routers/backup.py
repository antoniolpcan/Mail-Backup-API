from functions import get_email
from functions.__init__ import get_mail
from vars import zip_format,ziped_dir,router_names
from fastapi.responses import FileResponse
from .router_config import router
from fastapi import Depends

@router.post(router_names[1])
async def mail_backup(name = Depends(get_mail)):
    return FileResponse(path = f'{ziped_dir}{name}',filename = f'{name}',media_type=f"{zip_format}")