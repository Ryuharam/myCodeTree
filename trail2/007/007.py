secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class code:
    def __init__(self, secret, place, time):
        self.secret = secret
        self.place = place
        self.time = time


mycode = code(secret_code, meeting_point, time)
print(f'secret code : {mycode.secret}\nmeeting point : {mycode.place}\ntime : {mycode.time}')