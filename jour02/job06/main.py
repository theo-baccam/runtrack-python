def check_prem(num):
    if int(num) <= 1:
        return False
    elif int(num) == 2:
        return True
    elif int(num) % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if int(num) % i == 0:
                return False
        return True

for i in range(1, 1001):
    if not check_prem(i):
        continue
    print(i)