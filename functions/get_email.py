from .check.__init__ import check_files,check_deleted
from .directory.__init__ import get_zip,bup

def get_mail(site,email,senha):
    """
    Faz o backup e retorna um arquivo zipado
    """
    lista_arq_old = check_files(site,email)[0]
    lista_dir = check_files(site,email)[1]
    new_titles = bup(site,email,senha,lista_arq_old)
    check_deleted(lista_arq_old,lista_dir,new_titles,site,email)
    name = get_zip(site,email)
    return name
    
    

                    
    
    
                