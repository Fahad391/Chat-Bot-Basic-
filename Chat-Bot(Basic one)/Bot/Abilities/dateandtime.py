from datetime import datetime

def Date():
    date = datetime.now().date().strftime("%d-%m-%Y")
    return date
def Time():
    time = datetime.now().time().strftime("%H:%M:%S")
    return time