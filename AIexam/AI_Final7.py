def logic_eval(FR, TR, SV, PS=True, D=True):
    I1 = FR and TR
    I2 = TR or SV
    I3 = FR and not (SV or PS)
    I4 = (FR and TR) or PS
    I5 = not (PS or D) or FR
    I6 = I2 or I3
    I7 = I6 or (I4 if I5 else not I4)
    I8 = I7  # Assuming stabilization of the self-implicating structure
    return I8

# Generating the truth table
inputs = [(FR, TR, SV, PS) for FR in [False, True] for TR in [False, True] for SV in [False, True] for PS in [False, True] ]
results = []

for FR, TR, SV, PS in inputs:
    result = logic_eval(FR, TR, SV, PS)
    results.append((FR, TR, SV, PS, result))

# Printing the results
for line in results:
    print(f"FR: {line[0]}, TR: {line[1]}, SV: {line[2]}, PS: {line[3]}, isSuccessful: {line[4]}")
    


