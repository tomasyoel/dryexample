# Non-DRY Version (Repeated Logic)
def convert_temps_non_dry(fahrenheit_list):
    celsius_list = []
    for f in fahrenheit_list:
        celsius_list.append((f - 32) * 5/9)  # Repeated formula
    return celsius_list

# DRY Version (Centralized Logic)
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9  # Single source of truth

def convert_temps_dry(fahrenheit_list):
    return [fahrenheit_to_celsius(f) for f in fahrenheit_list]

# Test
temps_f = [32, 68, 100, 212]
print("Non-DRY:", convert_temps_non_dry(temps_f))
print("DRY:", convert_temps_dry(temps_f))