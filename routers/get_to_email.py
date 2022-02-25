from functions.__init__ import send_to_email
from vars import router_names
from .router_config import router
from fastapi import Body

@router.post(router_names[2])
def to_email(email = Body(...),senha = Body(...),site = Body(...),mes = Body(...),ano = Body(...)):
    response = send_to_email(email,senha,site,mes,ano)
    return response
