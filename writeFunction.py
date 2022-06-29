def is_leap(y):
    
    if 1900 <= y <= 10**5:
        if (y%4==0 and y%100!=0) or (y%100==0 and y%400==0):
            return True
        else:
            return False
    else:
        return False
year = int(input())
print(is_leap(year))
