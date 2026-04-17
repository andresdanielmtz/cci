def isCardVisa(cardNumber: str) -> bool:
    return cardNumber.startswith("4")

def isCardMastercard(cardNumber: str) -> bool:
    firstTwoDigits = int(cardNumber[:2])
    firstFourDigits = int(cardNumber[:4])
    
    isCardNumberBetweenOldRange = firstTwoDigits >= 51 and firstTwoDigits <= 55
    isCardNumberBetweenNewRange = firstFourDigits >= 2221 and firstFourDigits <= 2720
    
    return isCardNumberBetweenOldRange or isCardNumberBetweenNewRange

def isCardVisaOrMastercard(cardNumber: str) -> str:
    result = ""
    if isCardVisa(cardNumber):
        result = "Visa"
    if isCardMastercard(cardNumber):
        result = "Mastercard"
    return result


