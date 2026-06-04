Y, M, D = map(int, input().split())

# Please write your code here.
def get_season(month:int)->str:
    if month>=3 and month<=5:
        return 'Spring'
    if 6<=month and month<=8:
        return 'Summer'
    if 9<=month and month<=11:
        return 'Fall'
    return 'Winter'

def is_leap_year(year: int)->bool:
    if year%400==0:
        return True
    if year%100==0:
        return False
    return year%4==0


def check_day(year:int, month:int, day: int)->bool:
    if month == 2:
        if is_leap_year(year):
            return day<=29
        return day<=28
    
    if month in [1,3,5,7,8,10,12]:
        return day <= 31
    return day <=30

if check_day(Y,M,D):
    print(get_season(M))
else:
    print(-1)
