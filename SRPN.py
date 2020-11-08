import re

# Check if input value is a number
def number(value):
  try:
    value = int(value)
  except ValueError:
    return False
  return True
# Check if input value is an operator
def operator(text):
  operators = ['+', '-', '*', '/', '%', '^']
  if text in operators:
    return True
  else:
    return False

# Saturation values
max_value = 2147483647
min_value = -2147483648

# Perform arithmetic operations on a SRPN stack

def calc(op1, op2, operator):

  # Calculate based on operator
  if operator == '+':
    return max(min(op1 + op2, max_value), min_value)
  elif (operator == '-'):
    return max(min(op1 - op2, max_value), min_value)
  elif operator == '*':
    return max(min(op1 * op2, max_value), min_value)
  elif operator == '%':
    return max(min(op1 % op2, max_value), min_value)
  elif operator == '^':
    return max(min(op1 ** op2, max_value), min_value)
  else:
    try:
      res = max(min(op1 / op2, max_value), min_value)
      return res
    except ZeroDivisionError:
      return False

# Define random numbers function
def random_numbers(index):
  randomList = [1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368]
  if index < len(randomList):
    return randomList[index]
  else:
    return False

# Removing comments using regular expression
def remove_comments(text):
  text = str(text)
  return re.sub(r'(?m)^ *#.*\n?', '', text)


# Get input and perform operations for a SRPN stack

def operate_srpn_stack():
  print('You can now start interacting with the SRPN calculator')
  stack = []
  result = 0
  random_index = 0

  while True:
    value = input('')
    value = remove_comments(value)
    value = value.split()

    for _ in value:
      if number(_):
         # Append number to stack
        stack.append(int(_))
      elif operator(_):
        # Calculate and append result to stack (unless there is a division by zero error)
        if len(stack) > 1:
          op2 = stack.pop()
          op1 = stack.pop()
          if op2 != 0:
            result = calc(op1, op2, _)
            stack.append(result)
          else:
            print('Divide by 0.')
            break
        else:
          print('Stack underflow')
          break
      elif _ == 'r':
        randomNum = random_numbers(random_index)
        if randomNum:
          stack.append(randomNum)
          random_index += 1
        else:
          print ('Stack overflow')
      elif _ == 'd':
         # Print entire stack
        for value in stack:
          print(value)
      elif _ == '=':
        if len(stack) > 0:
           # Print top of the stack
          print (int(stack[-1]))
        else:
          print('Stack underflow')
        break
      else:
        print('Unrecognised operator or operand "%s".' %_)
        break


# Main program entry point

if __name__ == '__main__':
  operate_srpn_stack()