from functions.__init__ import send_to_email
from fastapi import Depends
from .router_config import router

@router.get('/email')
def to_email(response = Depends(send_to_email)):
    return response
