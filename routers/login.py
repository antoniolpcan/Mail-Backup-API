from functions.__init__ import login_email
from .router_config import router
from vars import router_names
from fastapi import Depends

@router.post(router_names[0])
def login(login_info = Depends(login_email)):
    return login_info