from functions.__init__ import login_email
from .router_config import router
from vars import router_names
from fastapi import Body

@router.post(router_names[0])
def login(email = Body(...),password = Body(...),site = Body(...)):
    login_info = login_email(email,password,site)
    return login_info