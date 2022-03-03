from functions.__init__ import get_mail
from vars import router_names
from .router_config import router
from fastapi import Depends
#from vars import zip_format,ziped_dir
#from fastapi.responses import FileResponse

@router.post(router_names[1])
async def mail_backup(response = Depends(get_mail)):
    #name = response.get('Name_file')
    print(response)
    return response
    #return FileResponse(path = f'{ziped_dir}{name}',filename = f'{name}',media_type=f"{zip_format}")