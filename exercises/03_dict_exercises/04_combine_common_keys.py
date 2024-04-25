# Write a Python program to combine two dictionary adding values for common keys.
# Expected output: d3 = {'a': 400, 'b': 400, 'c': 300, 'd': 350}

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':350}

d3 = d1.copy()
for k in d2:
    if k in d3:
        d3[k] = d2[k] + d3[k]
    else:
        d3[k] = d2[k]
print(f"{d3 = }")