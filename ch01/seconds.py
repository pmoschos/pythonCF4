# day - time counter

# giving seconds
total_seconds = 105310

# Calculating the number of days
days = total_seconds // (24 * 60 * 60)

# caclutale the remaining seconds
remaining_secods = total_seconds - (days * 24 * 60 * 60)

# number of hours
hours = remaining_secods // (60 * 60)
