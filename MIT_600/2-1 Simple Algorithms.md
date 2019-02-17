# 3. Simple Algorithms

## So Far...

- strings are "immutable" - cannot be modified

```python
s = "hello"
s[0] = 'y' # gives an error
s = 'y' + s[1:len(s)] # is allowed. s is a new object
```

binding of s : hello -> yello



## Approximate Solutions

### idea

- "good enough" solution
- start with a guess and increment by some "small value"
- `|guess^3| - cube <= epsilon` for some "small epsilon"
- decreasing increment size => slower program
- increasing epsilon => less accurate answer



### searching cube root

```python
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cub) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
```





### Some observations

- Step could be any small number
  - If too small, takes a long time to find square root
  - If too large, might skip over answer without getting close enough
- In general, will take x/step times through code to find solution
- Need a more effcient way to do this





## Bisection Search

```python
x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x: ### 여기 부분을 'ans < x**(1/2)'라고 이해하면 편하다 ###
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
```

- search space

  - first guess : N/2
  - second guess : N/4
  - gth guess : N/2**g

- guess converges on the order of log2N steps

- bisection search works when value of function varies monotonically with input

- code as shown only works for positive cubes > 1 - why?

- challenges

  -> modify to work with negative cubes!

  -> modify to work with x < 1



### Some observations

- Bisection search radically reduces computation time - being smart about generating guesses is important
- Sould work well on problems with "ordering" property - value of function being solved varies monotonically with input value
  - Here function is g**2; which grows as g grows





## Floats and Fractions

### Converting decimal integer to binary

```python
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
if isNeg:
    result = '-' + result
```



### What about fractions?

- 3/8 = 0.375
- So if we muliply by a power of 2 big enough to convert into a whole number(정수), can then convert to binary, and then divide by the same power of 2
- 0.375 * (2**3) = 3 (decimal)
- Convert 3 to binary (now 11)
- Divide by 2**3 (shift right) to get 0.011 (binary)

```python
x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2
    
for i in range(p - len(result)):
    result = '0' + result
    
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x))
```



### Some implications

- If there is no integer p such that x*(2**p) is a whole number, then internal representation is always an approximation
- Suggest that testing equality of floats is not exact
  - Use abs(x-y) < some small number, rather than x == y
- Why does print(0.1) return 0.1, if not exact?
  - Because Python designers set it up this way to automatically round

cf. The internal representation of the decimal number 1/10 = 0.1 requires an infinite number of digits.





## Newton-Raphson

- General approximation algorithm to find roots of a polynomial in one variable

  `p(x) = a(n)x**n + a(n-1)x**(n-1) + ... + a(1)x + a(0)`

- Want to find r such that p(r) = 0

- For example, to find the square root of 24, find the root of p(x) = x^2 - 24

- Newton showed that if g is an approximation to the root, then

  `g - p(g)/p'(g)`

  is a better approximation; where p' is derivative of p



- Simple case : `cx^2 + k`

- First derivative : `2cx`

- So if polynomial is `x^2 + k`, then derivative is `2x`

- Newton-Raphson says given a guess g for root, a better guess is

  `g - (g^2 - k)/2g`

  

```python
epsilon = 0.01
y = 54.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess (((guess**2) - y)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
```



### Iterative algorithms

- Guess and check methods build on reusing same code
  - Use a looping construct to generate guesses, then check and continue
- Generating guesses
  - Exhaustive enumeration
  - Bisection search
  - Newton-Raphson (for root finding)