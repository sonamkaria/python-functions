# Write a function named sum_tothat accepts 
# a single integer, n, and returns the sum of the integers from 1 to n.
# example: 
# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_tothat(n):
    total=[]
    for n in range(1 , n + 1):
            total.append(n)
            n = (n + 1)
    return(sum(total))

print(sum_tothat(6))

# Write a function named largest that takes a list of numbers 
# as an argument and returns the largest number in that list.
# For example:
# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(list):
     list.sort()
     print("Largest element is:", max(list))

numbers=[1,2,76,8,566]
largest(numbers)

# Write a function named occurances that takes two string arguments 
# as input and counts the number of occurances of the second string
# inside the first string.
# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

def occurances(string, sub_string):
    return string.count(sub_string)

print(occurances('fleep floop', 'ee'))


# Write a function named productthat takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

def product(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(product(-1, 4))