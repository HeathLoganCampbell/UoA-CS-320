# Fast Fourier Transform

## What is fourier analysis
* it's a method of signal processing
* a function is a sum of sin waves
  * This means you can make any function (saw, square) with only sin
  * but it might require infinite number of waves to appear the same 1 to 1

### Fourier Transform
* Time domain to Frequency domain
![Domain and Frequency domain](./note-resources/timeAndFrequency.gif)

### Polynomials: 
#### coefficient representation
A(x) = a_0 + a+1 * x + ... + a_n-1 * x^(n-1)
B(x) = b_0 + b+1 * x + ... + b_n-1 * x^(n-1)

Adding
* run time is O(n)
  * Because we just go through them one by one

Evaluation
* run time is O(n)
* using horner's method

Multiplication
* run time is O(n^2)
* using bruteforce
* A(x) * B(x)

#### Point value representation
Algebra fundament theorems
*   a univerariate polynomial of degree n with complex coefficients has exactly n complex roots
*   A univerariate polynomial of degree n - 1 is uniquely specified by it's evaluation at n distinct valies of x
d(x) = 1 + x = degree 1, we only need 2 points to find the line
t(x) = 1 + 2x + 3x^2 = degree 3, we need 3 points to get a probaler (x^2)

A(X) = f(x) -> {}
B(x) = g(x)

f(x)+g(x)

### Overalll picture
We n eed a fast way to convert between coefficient representation to point value repesentation.
which is where FFT with O(n log n) time, as well as inverse FFT at O(n log n) too to go back.
