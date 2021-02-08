from replit import clear

#Calculation
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

  
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


def calculator():
  should_calculate = True
  while should_calculate:
    num1 = float(input("What's the first number?: "))
    for symbol in operations: 
      print(symbol)

    should_continue = True
    while should_continue:
      operation_symbol = input("Pick an operation: ")
      num2 = float(input("What's the next number?: "))

      answer = operations[operation_symbol](num1, num2)

      print(f"{num1} {operation_symbol} {num2} = {answer}.")

      continue_calculation = input(f"Type 'y' to continue calculating with {answer}, type 'a' to start a new calculation or type 'n' to exit: ")

      if continue_calculation == "y":
        num1 = answer
      elif continue_calculation == "a":
        clear()
        calculator()
      else: 
        should_continue = False
        should_calculate = False
        clear()
        print("Have a nice day! 🧚")
      
calculator()
