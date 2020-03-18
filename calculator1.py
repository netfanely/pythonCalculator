#Python Calculadora simple

print("1. Suma");
print("2. Resta");
print("3. Multiplicacion");
print("4. Division");
print("5. Salir");
choice = int(input("Entre su opción: "));
if choice>=1 and choice<=4):
  printf("Ingrese dos números: ");
  num1 = int(input());
  num2 = int(input());
  if choice == 1:
      res = num1 + num2;
      print("Result = ", res);
  elif choice == 2:
      res = num1 - num2;
      print("Result = ", res);
  elif choice == 3:
      res = num1 * num2;
      print("Result = ", res);
  else:
      res = num1 / num2;
      print("Result = ", res);
  elif choise == 5:
      exit();
  else:
      print("Wrong input..!!");
      
