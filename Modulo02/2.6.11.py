hora = int(input("Digite as horas: "))
mins = int(input("Digite os minutos: "))
durac = int(input("Digite a duração: "))

hora_to_mins =  hora * 60
hora_mins_sum = hora_to_mins + mins + durac
if hora > 0 and hora < 24:
    if mins > 0 and mins < 60:
        result_h = (hora_mins_sum // 60) % 24
        result_min = hora_mins_sum % 60

        print("O evento terminará às: " + str(result_h) + ":" + str(result_min))