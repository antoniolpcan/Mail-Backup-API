from functions.__init__ import login_email
from fastapi import Depends
from .router_config import router

@router.post('/login')
def login(login_info = Depends(login_email)):
    return login_info