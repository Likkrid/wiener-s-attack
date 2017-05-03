========================
Mini Project
Wiener's attack on RSA
========================

To make the public key of RSA cryptosystem to vulnerable to Wiener's attack. We have to take prime numbers p and q such that q<p<2*q.

The file rsa_wiener.py generates the public key and private key if two prime numbers is given as input. Input prime numbers such that q<p<2*q. Now the public key is vulnerable to Wiener's attack.

The second file wiener.py contains the implementation of Wiener's attack.
Input to be given is product of primes: n (p*q) and b(encryption exponent) generated using first program. Then the output will be the two prime numbers which are private keys.

Wiener's attack is based on continued fractions.

For more:
https://en.wikipedia.org/wiki/Wiener's_attack
https://en.wikipedia.org/wiki/Continued_fraction
