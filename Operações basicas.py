def main():
  num1 = int(input("digite un numero: "))
  num2 = int(input("digite outro numero: "))

  soma = num1 + num2
  sub = num1 - num2
  mult = num1 * num2
  div = num1 / num2

  print("a soma é: ", num1," + ",num2," = ", soma)
  print("a soma é:",num1," - ",num2," = ",sub)
  print("a soma é:",num1," * ",num2," = ",mult)
  print("a soma é:",num1," / ", num2," = ",div)
  return 0
main()