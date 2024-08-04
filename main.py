from art import logo

# Calculator actions

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Dictionary

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

# ---------------------------------------------------------------------------

def calculator():
  print(logo)
  num1 = float(input("What's the first number?\n"))
  for keys in operations:
    print(keys)
  
  end_of_calculation = False
  
  while end_of_calculation == False:
    
    operation_symbol = input("Pick an operation:\n")
    num2 = float(input("What's the next number?\n"))
    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    continue_calculating = input(f"Yype 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:\n")
    
    if continue_calculating == "y":
      num1 = answer
    else:
      end_of_calculation = True
      calculator()

calculator()