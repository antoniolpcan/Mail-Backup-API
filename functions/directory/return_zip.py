from functions.treat_values.__init__ import format_date
from .remove_dir import rm_dir
from vars import zip_format,email_dir,ziped_dir,date_time
from shutil import make_archive
from datetime import datetime

def get_zip(site,email):
    """
    Compacta a pasta backup.
    """
    data = datetime.today().strftime(date_time)
    tdata = format_date(data)
    
    try:
        rm_dir(ziped_dir)
    except:
        print(f"Diretorio '{ziped_dir}' será criado")

    make_archive(f'{ziped_dir}{email}_{tdata}', f'{zip_format}', f'{email_dir}{site}/{email}')
    print(f"Arquivo '{email}_{tdata}.{zip_format}' foi retornado.")
    name = f"{email}_{tdata}.{zip_format}"
    return name