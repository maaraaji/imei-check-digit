def checkDigitCalc(tacPlusSerial):
    doubledResult = []
    [doubledResult.append(int(str(int(x) * 2)[0]) + int(str(int(x) * 2)[1]) if len(str(int(x) * 2)) == 2 else int(x) * 2) if i % 2 != 0 else doubledResult.append(int(x)) for i, x in enumerate(str(tacPlusSerial))]
    return int(str(tacPlusSerial) + str(10 - (sum(doubledResult) % 10)))

def luhn_residue(digits):
    return sum(sum(divmod(int(d)*(1 + i%2), 10)) for i, d in enumerate(digits[::-1])) % 10

tacPlusSerial = 35913906398494
imei = checkDigitCalc(tacPlusSerial)
print("TAC Plus Serial Number : ", tacPlusSerial)
print("Calculated IMEI Number : ", imei)
imeil = luhn_residue(tacPlusSerial)
print(imeil)