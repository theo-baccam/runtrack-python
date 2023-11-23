numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

rounded_numbers = [int(num) for num in numbers]

n = 0
for _ in rounded_numbers:
    n += 1

for i in range(n):
    for j in range(0, n-i-1):
        if rounded_numbers[j] > rounded_numbers[j+1]:
            rounded_numbers[j], rounded_numbers[j+1] = rounded_numbers[j+1], rounded_numbers[j]

print(rounded_numbers)