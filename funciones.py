import time
def validateDateEs(date):
    for format in ['%d/%m/%Y', '%d/%m/%y', '%d/%m/%Y %H:%M:%S', '%d/%m/%y %H:%M:%S']:
        try:
            result = time.strptime(date, format)
            return True
        except:
            pass
    return False