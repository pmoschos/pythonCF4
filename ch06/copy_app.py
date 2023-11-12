import copy

ages = [23, 45, 36]

# Shallow copy
ages_cp = ages.copy()

# Deep copy (using 'copy' module)
ages_dcp = copy.deepcopy(ages)

