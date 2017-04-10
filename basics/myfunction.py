def minutes_to_hours(minutes):
    hours = minutes/60
    return hours

def seconds_to_hours(seconds):
    hours = seconds/3600
    return hours

def minutes_seconds(seconds, minutes=50):
    hours = minutes/60 + seconds/3600
    return hours


print(minutes_to_hours(90))

print(seconds_to_hours(6000))


print(minutes_seconds(3600))


def printing():
    print('-'*100)
    print("This is a printing function.")
    print('-'*100)


printing()
