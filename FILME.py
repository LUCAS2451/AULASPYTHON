def main():
  idade = int(input("digite sua idade: "))

  if idade >= 18:
    print("entrada liberada")
  elif idade >= 16:
    acompanhante = input("tem acompanhante? (s/n) ")
    if acompanhante =="s":
      print("entrada liberada")
    else:
      print("entrada proibida!")
  else:
    print("entrada proibida!")
    
  return 0
main()