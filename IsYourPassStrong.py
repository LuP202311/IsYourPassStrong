import re

def isMDPLong(MDP):
    isLong = True
    message = ""
    if len(MDP) < 8:
        isLong = False
        message = "Le mot de passe est très faible"
    elif 8 <= len(MDP) <= 12:
        isLong = False
        message = "Le mot de passe est faible"
    elif 12 < len(MDP) <= 16:
        isLong = True
        message = " "
    else:
        isLong = True
        message = " "
    
    return isLong, message

def usedAllCharac(MDP):
    if re.findall(r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])", MDP):
        hasAllCharac = True
        messageC = " "
    else:
        hasAllCharac = False
        messageC = "Le mot de passe doit contenir au moins un chiffre, une lettre en majuscule et minuscule"
    return messageC, hasAllCharac
    
saisie = input("Veuillez saisir le mot de passe: ")
isLong, message = isMDPLong(saisie)
messageC, hasAllCharac = usedAllCharac(saisie)

while not isLong or not hasAllCharac:
    print(message + "\n" + messageC)
    resaisie = input("Veuillez re-saisir le mot de passe: ")
    isLong, message = isMDPLong(resaisie)
    messageC, hasAllCharac = usedAllCharac(resaisie)

print(message + "\n" + messageC)