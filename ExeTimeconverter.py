#Programa para convertir horarios de de PM/AM a 24 horas | test de HackerRank

#Ingresa formato hh:mm:ssPM y sale formato hh:mm:ss en horario militar

def timeConversion(s):
    hh= int((s[0:2]))
    mm=((s[3:5]))
    ss=((s[6:8]))
    AMPM = (s[8:10])
    if AMPM == 'PM':
        if hh == 12:
            hh = hh
        else:
            hh =  hh + 12
    elif AMPM =='AM':
        hh = hh
        if hh == 12:
            hh = str('00')
        elif hh < 10:
            thh =str(hh)
            hh = str('0'+ thh)
    shh=str(hh)
    smm=str(mm)
    sss=str(ss)
    hora = shh +':'+ smm +':'+ sss
    return (hora)

s = input('Ingrese la hora en formato hh:mm:ssPM/AM: ')
result = timeConversion(s)
print (result)
