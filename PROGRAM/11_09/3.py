from input_check import input_float

def tf_tc(tf: float):
    return (tf - 32) / 1.8


tf1 = 59
tc1 = tf_tc(tf1)
print(f"1. {tc1}°C = {int(tf1)}°F")

tf2 = input_float("Введите температуру в °F: ")
tc2 = tf_tc(tf2)
print(f"2. {round(tc2, 2)}°C = {round(tf2, 2)}°F")
