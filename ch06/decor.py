import time

def get_time(n):
    star_time = time.time()
    # make my calculations
    result = sum(range(n)) # 0 + 1 + 2 + 3 + ... + (n - 1)
    end_time = time.time()
    print(f"My function took {end_time - star_time: .5f} seconds to run")

    return result

print(get_time(1000000))
    