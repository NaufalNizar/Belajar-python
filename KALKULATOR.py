print("KALKULATOR\n")
x = float(input("masukan nilai pertama:"))
print("")
op = (input("operasi +/-/x/:\n"))
y = float(input("masukan nilai kedua:"))
if op == "+":
    hasil = x + y
    print(f"hasil :  {hasil}")
elif op == "x":
    hasil = x * y
    print(f"hasil :  {hasil}")
elif op == ":":
    if y == 0:
        print("ERROR")
    else:
        hasil = x / y
        print(f"hasil :  {hasil}")
else:
    print("perintah tidak diketahui")
