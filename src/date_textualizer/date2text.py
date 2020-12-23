from datetime import date

days = [
    ['hétfő', 'hétfőn'],
    ['kedd', 'kedden'],
    ['szerda', 'szerdán'],
    ['csütörtök', 'csütörtökön'],
    ['péntek', 'pénteken'],
    ['szombat', 'szombaton'],
    ['vasárnap']
]


def is_day_of(d):
    return days[d.weekday()][-1]


def date2text(d: date, now: date):
    resp = ''
    day_diff = (d - now).days
    till_next_week = 7 - now.weekday() - 1

    if day_diff == 0:
        resp += 'ma'
    elif day_diff == 1:
        resp += 'holnap'
    elif day_diff < till_next_week:
        resp += 'ezen a héten ' + is_day_of(d)
    elif till_next_week < day_diff <= till_next_week + 7:
        resp += 'jövőhét ' + is_day_of(d)
    elif till_next_week + 7 < day_diff <= till_next_week + 14:
        resp += 'két hét múlva ' + is_day_of(d)
    else:
        resp += f'ekkor: {d.year}-{d.month}-{d.day}, {is_day_of(d)}'

    return resp
