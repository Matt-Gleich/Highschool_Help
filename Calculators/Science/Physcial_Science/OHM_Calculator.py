# Instructions:
# Just run the file and answer the questions!
# --------------------------------------------------------------------
random_continious_number = 0
while random_continious_number == 0:
    exchange = input("What are you trying to find (Voltage, Current(Ampage), or Resistance)\n")
    if "vol" in exchange.lower():
        print("")
        amps = input("What is the amount of amps?\n")
        print("")
        resistance = input("What is the amount of resistance?\n")
        print("")
        amps_int = float(amps)
        resistance_int = float(resistance)
        voltage = amps_int * resistance_int
        print("The voltage is:",voltage,"volts\n")
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            continue
        else:
            break
    elif "cur" in exchange.lower():
        print("")
        volts = input("What is the amount of volts?\n")
        print("")
        resistance = input("What is the amount of resistance?\n")
        print("")
        volts_int = float(volts)
        resistance_int = float(resistance)
        current = volts_int / resistance_int
        print("The current(Ampage) is:",str(current)+"amps\n")
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            continue
        else:
            break
    elif "res" in exchange.lower():
        print("")
        volts = float("What is the amount of volts?\n")
        print("")
        amps = float("What is the amount of amps?\n")
        print("")
        volts_int = float(volts)
        amps_int = float(amps)
        resistance = volts_int / amps_int
        resistance_str = str(resistance)
        print("The resistance is:",resistance_str,"(Ohms)")
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            continue
        else:
            break
    else:
        print("Please put in a valid input!")
        continue
