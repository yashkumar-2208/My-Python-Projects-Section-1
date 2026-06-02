class Unit_Convertor():

    @staticmethod
    def unit_conversion():

        print("-- Press the numbers --")
        print("Press '1' for length conversion")
        print("Press '2' for mass/weight conversion")
        print("Press '3' for time conversion")
        print("Press '4' for area conversion")
        print("Press '5' for volume conversion")
        print("press '6' for speed conversion")
        print("Press '7' for data storage conversion")
        print("Press '8' for energy conversion")
        print("Press '9' for pressure conversion")
        print("             --")

        try:

            while True:

                user_input = int((input("Enter your number here: ")))

                if user_input == 1:
                    print("You have chosen length conversion!")
                    print("Given below are the available conversion operation")
                    print("Press '1' to convert Meter → Centimeter ")
                    print("Press '2' to convert Meter → Kilometer")
                    print("Press '3' to convert Kilometer → Meter")
                    print("Press '4' to convert Inch → Centimeter")
                    print("Press '5' to convert Foot → Meter")
                    print("Press '6' to convert Meter → Foot")
                    print("Press '7' to convert Mile → Kilometer ")

                    user_choice = int((input("Enter length conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))
                    

                    if user_choice == 1:
                        print(f"You've chose {user_choice}")
                        print(f"Your converted value is: {units * 100}cm")

                    elif user_choice == 2:
                        print(f"You have chosen {user_choice}")
                        print(f"Your converted value is: {units / 1000}km")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}m")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 2.54}cm")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.3048}m")

                    elif user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3.28084}ft")

                    elif user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1.60934}km")

                    else:
                        print("Choose between (1 to 7)")


                elif user_input == 2:
                    print("You've chosen mass/weight conversion")
                    print("Given below are the available conversion operation")
                    print("Press '1' to convert Kilogram → Gram")
                    print("Press '2' to convert Gram → Kilogram")
                    print("Press '3' to convert Pound → Kilogram")
                    print("Press '4' to convert Kilogram → Pound")
                    print("Press '5' to convert Ton → Kilogram")

                    user_choice = int((input("Enter Mass/Weight conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units *1000}g")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units/1000}kg")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.453592}kg")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 2.20462}lb")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}kg")

                    else:
                        print("Choose number between (1 to 5) only")

                elif user_input == 3:
                    print("You've chosen Time conversion")
                    print("Given below are the available conversion operation")
                    print("Press '1' to convert Minute → Second")
                    print("Press '2' to convert Hour → Minute")
                    print("Press '3' to convert Day → Hour")
                    print("Press '4' to convert Week → Day")
                    print("Press '5' to convert Year → Day")

                    user_choice = int((input("Enter Time conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 60}sec")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 60}min")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 24}hr")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 7}day")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 365}day")

                    else:
                        print("Choose number between (1 to 5) only")


                elif user_input == 4:
                    print("You've chosen Area conversion")
                    print("Given below are the available conversion operation")
                    print("Press '1' to convert m² → cm²")
                    print("Press '2' to convert km² → m²")
                    print("Press '3' to convert Acre → m²")
                    print("Press '4' to convert Hectare → m²")

                    user_choice = int((input("Enter Area conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 10000}cm²")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000000}m²")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 4046.86}m²")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 10000}m²")
                    else:
                        print("Choose number between (1 to 4) only!")

                elif user_input == 5:
                    print("You've chosen Volume conversion")
                    print("Given below are the available conversion operation")
                    print("Press '1' to convert Liter → Milliliter")
                    print("Press '2' to convert Milliliter → Liter")
                    print("Press '3' to convert Cubic Meter → Liter ")
                    print("Press '4' to convert Gallon (US) → Liter")

                    user_choice = int((input("Enter Volume conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))


                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}ml")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000}l")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}l")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3.78541}l")
                    else:
                        print("Choose number between (1 to 4) only!")


                elif user_input == 6:
                    print("You've chosen Speed conversion")
                    print("Given below are the available conversion operation")
                    print("Press '1' to convert km/h → m/s")
                    print("Press '2' to convert m/s → km/h")
                    print("Press '3' to convert mph → km/h")

                    user_choice = int((input("Enter Speed conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))


                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 3.6}m/s")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3.6}km/h")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1.60934}km/h")

                    else:
                        print("Choose number between (1 to 3) only!")

                elif user_input == 7:
                    print("You've chosen Data Storage conversion")
                    print("Given below are the available conversion operation")
                    print("Press '1' to convert Byte → Bit")
                    print("Press '2' to convert KB → Byte")
                    print("Press '3' to convert MB → KB")
                    print("Press '4' to convert GB → MB")
                    print("Press '5' to convert TB → GB")

                    user_choice = int((input("Enter Speed conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))


                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 8}bit")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1024}B")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1024}KB")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1024}MB")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1024}GB")

                    else:
                        print("Choose number between (1 to 5) only!")


                elif user_input == 8:
                    print("You've chosen Energy conversion")
                    print("Given below are the available conversion operation")
                    print("Press '1' to convert Calorie → Joule")
                    print("Press '2' to convert Joule → Calorie")
                    print("Press '3' to convert kWh → Joule")

                    user_choice = int((input("Enter Energy conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 4.184}J")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 4.184}cal")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3.6 * 1000000}J")

                    else:
                        print("Choose number between (1 to 3) only")

                elif user_input == 9:
                    print("You've chosen Pressure conversion")
                    print("Given below are the available conversion operation")
                    print("Press '1' to convert atm → Pascal")
                    print("Press '2' to convert bar → Pascal")
                    print("Press '3' to convert psi → Pascal")

                    user_choice = int((input("Enter Energy conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 101325}Pa")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 100000}Pa")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 6894.76}Pa")

                    else:
                        print("Choose number between (1 to 3) only!")

                else:
                    print("Enter available operation")

        except Exception as e:
            print(f"Error: {e}")


Unit_Convertor.unit_conversion()