def message_imc(x : int) -> str :
    if x < 16.5 :
        message = "dénutrition ou famine"
    elif x <= 18.5 :
        message ="maigreur"
    elif x <= 25 :
        message ="corpulence normale"
    elif x <= 30 :
        message ="surpoids"
    elif x <= 35 :
        message ="obésité modérée"
    elif x <= 40 :
        message ="obésité sévère"
    elif x > 40 :
        message ="obésité morbide"
    return message

msg=message_imc(10)
print("Vous êtes en situation de",msg,)
msg=message_imc(20)
print("Vous êtes en situation de",msg,)
msg=message_imc(30)
print("Vous êtes en situation de",msg,)
msg=message_imc(40)
print("Vous êtes en situation d'",msg,)
msg=message_imc(50)
print("Vous êtes en situation d'",msg,)