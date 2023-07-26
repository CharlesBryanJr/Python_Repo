'''temperature.py'''
print(" ")

class Temperature:

    min_temperature = 0
    max_temperature = 1000

    @classmethod 
    def update_min_temperature(cls, min_temperature):
        if min_temperature >= Temperature.max_temperature:
            raise ValueError("Error: min temperature must be less than max temperature")

        Temperature.min_temperature = min_temperature
    

    @classmethod 
    def updated_max_temperature(cls, max_temperature):
        if max_temperature <= Temperature.min_temperature:
            raise ValueError("Error: min temperature must be less than max temperature")

        Temperature.max_temperature = max_temperature
    

    def __init__(self, kelvin) -> None:
        
        if kelvin > Temperature.max_temperature:
            raise ValueError(f"Error: kelvin must be less than max temperature, {Temperature.max_temperature}")

        if kelvin < Temperature.min_temperature:
            raise ValueError(f"Error: kelvin must be greater than min temperature, {Temperature.min_temperature}")
        
        self.kelvin = kelvin

t = Temperature(999)

print(" ")