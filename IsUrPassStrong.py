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
        message = "Le mot de passe est robuste"
    else:
        isLong = True
        message = "Le mot de passe est très robuste"
    
    return isLong, message
    
saisie = input("Veuillez saisir le mot de passe: ")
isLong, message = isMDPLong(saisie)

while not isLong:
    print(message)
    saisie = input("Veuillez re-saisir le mot de passe: ")
    isLong, message = isMDPLong(saisie)

print(message)