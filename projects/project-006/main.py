# temperature only measure value between 15 degC to 30 degC

readings = [22.5, 14.2, 30.0, 31.7, 18.9, 15.0, -2.0, 27.3]

# define the data limits
MIN_TEMP = 15.0
MAX_TEMP = 30.0
N_TOO_LOW = 0    
N_TOO_HIGH = 0
N_VALID = 0
# write decision logic
for temp in readings:
    if temp < MIN_TEMP:
        N_TOO_LOW += 1
        print("TOO LOW")
    elif temp > MAX_TEMP:
        N_TOO_HIGH += 1
        print("TOO HIGH")
    else:
        N_VALID += 1
        print("VALID")

# Print report
print(f"Number of readings too low: {N_TOO_LOW}")
print(f"Number of readings too high: {N_TOO_HIGH}")
print(f"Number of valid readings: {N_VALID}")
