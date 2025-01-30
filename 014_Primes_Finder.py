
# Version 1
n = 20

number_range = set(range(2, n+1))
primrs_list = []

prime = number_range.pop()
primrs_list.append(prime)
multiples = set(range(prime*2, n+1, prime))
number_range.difference_update(multiples)


prime = number_range.pop()
primrs_list.append(prime)
multiples = set(range(prime*2, n+1, prime))
number_range.difference_update(multiples)


# Version 2

# upprt bound 
n = 1000

# number range to be checked
number_range = set(range(2, n+1))

# empty list to append discovered prime to
primes_list = []

# While loop
while number_range:
        prime = number_range.pop()
        primes_list.append(prime)
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples)

# print our list of primes        
print(primes_list)

# number of primes that were found
prime_count = len(primes_list)

# largest_prime 
largest_prime = max(primes_list)

# summary
print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime} ")



# Version 3


def primes_founder(n):
    # number range to be checked
    number_range = set(range(2, n+1))

    # empty list to append discovered prime to
    primes_list = []

    # While loop
    while number_range:
            prime = min(sorted(number_range))
            number_range.remove(prime)
            primes_list.append(prime)
            multiples = set(range(prime*2, n+1, prime))
            number_range.difference_update(multiples)


    # number of primes that were found
    prime_count = len(primes_list)

    # largest_prime 
    largest_prime = max(primes_list)

    # summary
    print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime} ")
    
    return primes_list


primes_list = primes_founder(100)
print(primes_list)


primes_list = primes_founder(10000000)
print(primes_list)

















































