from .format_data import format_date
import unicodedata
import re

def file_name_format(date,string,n):
    """
    Formata o nome do arquivo, retirando caracteres especiais e espaços e inserindo a data.
    """
    date = format_date(date)

    if string in ['',None,[]]:
        n = n + 1
        string = f"EmailSemTitulo_{n}_"

    string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]', '', string)
    processamento_2 = unicodedata.normalize("NFD", string_nova)
    processamento_3 = processamento_2.encode("ascii", "ignore")
    processamento_4 = processamento_3.decode("utf-8")
    treat_ch = processamento_4.replace(' ','_')
    treat_ch = f"{treat_ch}_{date}"
    return treat_ch