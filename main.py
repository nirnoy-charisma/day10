import art
print(art.logo)
#add
def add(n1, n2):
  return n1+n2
#subtract
def sub(n1, n2):
  return n1-n2
#multiply
def multiply(n1, n2):
  return n1*n2
#divide
def division(n1, n2):
  if n2 != 0:
      return n1 / n2
  else:
      return "Error: Division by zero"

operations = {
  "+":add, 
  "-":sub,
  "*":multiply ,
  "/":division
}
def calculator():
  num1= float(input("whats your first number? "))

  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
  
    symbol_choice= input("pick an operation from the line above ")
    num2= float(input("whats your next number? "))
    calculation_function= operations[symbol_choice]
    answer1= calculation_function(num1, num2)
    print (f"{num1} {operations}{num2} = {answer1}")
    if input(f"type 'y' to continue calculating with {answer1} or type 'n' to exit ")=="y":
       num1=answer1
    else:
     should_continue= False
     calculator()

calculator()
