
def add(a, b):
  sum =a+b
  return sum
  


def output(a, b, sum):
  print("the sum of {0} and {1} is 
  {2}".format(num1,num2,sum)))


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
