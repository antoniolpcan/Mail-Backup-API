from functions.__init__ import send_to_email
from vars import router_names
from .router_config import router
from fastapi import Depends

@router.post(router_names[2])
def to_email(response = Depends(send_to_email)):
    return response
