def checkDigitCalc(tacPlusSerial):
    doubledResult = []
    [doubledResult.append(int(str(int(x) * 2)[0]) + int(str(int(x) * 2)[1]) if len(str(int(x) * 2)) == 2 else int(x) * 2) if i % 2 != 0 else doubledResult.append(int(x)) for i, x in enumerate(str(tacPlusSerial))]
    return str(tacPlusSerial) + str(10 - (sum(doubledResult) % 10))

# tacPlusSerial = "35913906398494"
tacPlusSerial = "35499807155966"
imei = checkDigitCalc(tacPlusSerial)
print("TAC Plus Serial Number : " + tacPlusSerial)
print("Calculated IMEI Number : " + imei)
