from .check.__init__ import check_files,check_deleted
from .directory.__init__ import get_zip,bup
from fastapi import Body

def get_mail(site:str = Body(...),email:str = Body(...),senha:str = Body(...)):
    """
    Faz o backup e retorna um arquivo zipado
    """
    lista_arq_old = check_files(site,email)[0]
    lista_dir = check_files(site,email)[1]
    lista_new = bup(site,email,senha,lista_arq_old)
    new_titles = lista_new[0]
    new_mails = lista_new[1]
    deleted = check_deleted(lista_arq_old,lista_dir,new_titles,site,email)
    name = get_zip(site,email)
    return {"Email":email, "New_mails":new_mails, "Deleted":deleted, "Name_file": name}
    
    

                    
    
    
                