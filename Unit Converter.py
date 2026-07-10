

class Converter:
    
    def __init__(self) -> None:
        pass
    
    def length(self):
        length_units = {
            "km" :1000,
            "dcm":10,
            "m"  :1,
            "cm" :0.01,
            "mm" :0.001,
            "microm" :0.000001,
            "nanom" :0.000000001 
        }
        user_input = float(input("enter the number you want to convert :"))
        input_type = input("Enter the type of number you entered ( km / dcm / m / cm / mm / microm / nanom) :")
        output_type = input("Enter the type of number you want to convert to ( km / dcm / m / cm / mm / microm / nanom) :")
        result = user_input * length_units[input_type]/length_units[output_type]
        print(result)
                
    def mass(self):
        mass_units = {
            "kg" :1000,
            "pound" :0.00045,
            "gr" :1,
            "mg" :0.001
        }
        
        
        






