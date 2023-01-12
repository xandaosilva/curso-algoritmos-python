velocities = [100, 50, 80, 120, 70]
limit = 80

def check_speed_over_limit(velocity, limit):
    return True if velocity >= limit else False


print(f"Limit: {limit}")
for velocity in velocities:
    res = check_speed_over_limit(velocity, limit)
    print(f"Velocity: {velocity} - Speed over limit: {res}")

