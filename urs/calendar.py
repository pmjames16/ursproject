def monthtoname(num):
    if num == 1: return "January"
    elif num == 2: return "February"
    elif num == 3: return "March"
    elif num == 4: return "April"
    elif num == 5: return "May"
    elif num == 6: return "June"
    elif num == 7: return "July"
    elif num == 8: return "August"
    elif num == 9: return "September"
    elif num == 10: return "Octover"
    elif num == 11: return "November"
    elif num == 12: return "December"

def dayday(month):
    days = []
    if month == 11:
        #days = [30, 31]
        days = ["", ""]
        for i in range(30): days.append(i+1)
        #for i in range(3): days.append(i+1)
        for i in range(3): days.append("")
    elif month == 12:
        #days = [27,28,29,30]
        days = ["", "", "", ""]
        for i in range(31): days.append(i+1)
    elif month == 1:
        for i in range(31): days.append(i+1)
    return days

def daysweek(days):
    result = []
    while len(days)>7:
        result.append(days[:7])
        days = days[7:]
    if len(days)>0: result.append(days)
    return result

def times():
    result = []
    for i in range(24):
        result.append(i)
    return result