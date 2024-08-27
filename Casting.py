F_text = input("Enter the temp in degrees f: ")
F = float(F_text)
C = 5 * (F - 32) / 9
print("The temp in degrees c is", C)
C_text = input("Enter the temp in degrees C: ")
Cd = float(C_text)
Cd = 1.8 * Cd + 32
print("The temp in degrees f is", Cd)