# Sieve of Eratosthenes
The sieve of Eratosthenes is an ancient algorithm for finding all prime
numbers up to any given limit.  
It does so by iteratively marking as composite (i.e., not prime) the multiples
of each prime, starting with the first prime number, 2. The multiples of a
given prime are generated as a sequence of numbers starting from that prime,
with constant difference between them that is equal to that prime.[1] This is
the sieve's key distinction from using trial division to sequentially test
each candidate number for divisibility by each prime.

<img src="https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif" width="60%"/>

## Pseudocode
The sieve of Eratosthenes can be expressed in pseudocode, as follows:
```
algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.
    
    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
                A[j] := false

    return all i such that A[i] is true.
```
This algorithm produces all primes not greater than n. It includes a common optimization, which is to start enumerating the multiples of each prime i from i2. The time complexity of this algorithm is O(n log log n), provided the array update is an O(1) operation, as is usually the case.

## Implementation:
See the code implemention: [Sieve of Eratosthenes Code](sieve_of_eratosthenes.py)

Also see a faster way to get primes: [Sieve of Atkin](../sieve-of-atkin)

## Resources:
[Wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)