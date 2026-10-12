# Statistical Summary Calculator

values = [2.5, 4.0, 6.0, 8.0, 10.0]

count = len(values)
minimum = min(values)
maximum = max(values)
average = sum(values)/len(values)

print(f"""STATISTICAL SUMMARY
-----------------------------
Number of measurements: {count}
Minimum: {minimum}
Maximum: {maximum}
Mean: {average}
""")