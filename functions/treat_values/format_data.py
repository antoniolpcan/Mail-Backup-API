def format_date(date): 
    """
    Formata a data, substituindo espaços, traços e dois pontos por underline('_').
    """
    date = date.replace(' ','_').replace('-','_').replace(':','_')
    return date