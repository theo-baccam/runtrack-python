def time_to_text(num):
    hour = num // 60
    mins = num - (hour * 60) 

    print(f"{hour}h et", f"{mins}mins")

time_to_text(61)
time_to_text(160)
time_to_text(359)
time_to_text(38)