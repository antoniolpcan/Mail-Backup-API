from fastapi import HTTPException

def validate_date(month,year):

    if month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        print(f'O mês {month} é válido.')
    else:
        raise HTTPException(406,detail = f'O mês {month} é inválido')

    if len(year) != 4 or 2000>int(year) or int(year)>2100:
        raise HTTPException(406,detail = f'O ano {year} é inválido')