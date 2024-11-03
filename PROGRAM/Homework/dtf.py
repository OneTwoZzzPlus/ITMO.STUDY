import datetime

date = datetime.date
MAX_DATE = 32535205199

display_utc = lambda x: utc_to_datetime(x).strftime('%d.%m.%y')
display_data = lambda x: x.strftime('%d.%m.%y')

def utc_to_datetime(x: int):
    return datetime.date.fromtimestamp(x)

def datetime_to_utc(x: datetime.date): 
    return int(datetime.datetime(x.year, x.month, x.day).timestamp())

correct = lambda x: datetime_to_utc(utc_to_datetime(x))

now = lambda: datetime.date(
    datetime.datetime.now().year, 
    datetime.datetime.now().month, 
    datetime.datetime.now().day
)

def validate_point_date(r: str):
    try:
        rs = r.split('.')
        year = int(rs[2])
        
        if year < 100:
            year += 2000
        elif 100 <= year <= 1970 or year > 3000:
            raise ValueError

        return datetime.date(year, int(rs[1]), int(rs[0]))
    except (ValueError, TypeError, IndexError) as e:
        return None