# Task 1
# Implement conversion between the following units:
# Meters to kilometers
def m_to_km(meter):
    return meter / 1000

# Kilometers to meters
def km_to_m(kilometer): 
    return kilometer * 1000

# Meters to centimeters
def m_to_cm(meter):
    return meter * 100

# Centimeters to meters
def cm_to_m(centimeter):
    return centimeter / 100

# Task 2
# Temperature conversion

# Celsius to Fahrenheit
def degC_to_degF(degC):
    return 9/5 * degC + 32

# Fahrenheit to Celsius
def degF_to_degC(degF):
    return (5/9) * (degF-32)

# Task 3
# Pressure conversion

# Pascals to kilopascals
def Pa_to_kPa(Pa):
    return Pa / 1000

# Kilopascals to Pascals
def kPa_to_Pa(kPa):
    return kPa * 1000

print(f"""UNIT CONVERSION TOOLKIT
---------------------------------
Length:
1.5 km = {km_to_m(1.5)} m
250.00 cm = {cm_to_m(250)} m

Temperature:
25 degC = {degC_to_degF(25)} degF
32 degF = {degF_to_degC(32)} degC

Pressure:
101325 Pa = {Pa_to_kPa(101325)} kPa
100 kPa = {kPa_to_Pa(100)} Pa
""")

assert km_to_m(1.5) == 1500
assert cm_to_m(250) == 2.5
assert degC_to_degF(25) == 77
assert degF_to_degC(32) == 0
assert Pa_to_kPa(101325) == 101.325
assert kPa_to_Pa(100) == 100000