from gmpy import invert, root
from gmpy2 import mpz, get_context
import owiener


def multiplier(p, q):
    n = p*q
    return n


def divisor(n, div):
    a = n // div
    return a


def cal_phi(p, q):
    if(p != -1) and (q != -1):
        phi_n = (p-1)*(q-1)
        return phi_n
    else:
        print("P and Q is required to calculate phi N.")
        return 0


def modexp(base, exp, mod):
    value = base % mod
    for power in range(1, exp):
        value = (value*base) % mod
    return(value)


def mod_inverse(priv_key, phi_n):
    a = invert(priv_key, phi_n)
    return a


def std_decrypt(c, p, q, d):
    dp = d % (p-1)
    dq = d % (q-1)
    qinv = invert(q, p)

    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    h = (qinv * (m1-m2)) % p
    m = m2+h*q
    return m


def eth_root(cipher, e):
    get_context().precision = 1000
    e = mpz(e)
    cipher = mpz(cipher)
    a = root(cipher, e)

    if a**e == cipher:
        return ("Possible plaintext:", a)
    else:
        return("Problem with calculation...")


print("=====A wanna-be all in one textbook RSA solution=====")
print("Input everything you've known yet, leave others blank")
print("*****Currently doesn't support padding*****")

while True:
    print("Select operation:")
    print("=====Math part=====")
    print("1: Find N given P and Q")
    print("2: Find P/Q given N and P/Q")
    print("3: Find Phi N given P and Q")
    print("4: Mod Exponent (Encrypt/Simple Decrypt)")
    print("5: Mod Inverse (Find C/D)")
    print("6: Standard Decrypt (By part)")

    print("=====Attack part=====")
    print("7: Eth root attack")
    print("8: Wiener attack")
    print("0: To quit")

    x = int(input("Enter your choice:"))

    if x == 1:
        p = int(input("Enter P:"))
        q = int(input("Enter Q:"))
        print("N: ", multiplier(p, q))
        input("\nPress Enter to continue...")
    elif x == 2:
        p = int(input("Enter P/Q:"))
        n = int(input("Enter N:"))
        print("P or Q: ", divisor(n, p))
        input("\nPress Enter to continue...")
    elif x == 3:
        p = int(input("Enter P:"))
        q = int(input("Enter Q:"))
        print("Phi N: ", cal_phi(p, q))
        input("\nPress Enter to continue...")
    elif x == 4:
        t = int(input("Enter plaintxt/cipher:"))
        e = int(input("Enter E or D:"))
        n = int(input("Enter N:"))
        print("Encrypted/Decrypted text: ", modexp(t, e, n))
        input("\nPress Enter to continue...")
    elif x == 5:
        e = int(input("Enter known E or D:"))
        y = int(input("Enter 1 if you have PhiN, enter 2 if you have P and Q only"))
        if y == 1:
            phin = int(input("Enter Phi N:"))
            print("Pub/Priv key is: ", mod_inverse(e, phin))
        elif y == 2:
            p = int(input("Enter P:"))
            q = int(input("Enter Q:"))
            phin = cal_phi(p, q)
            print("Pub/Priv key is: ", mod_inverse(e, phin))
        else:
            print("Input error.")
        input("\nPress Enter to continue...")
    elif x == 6:
        p = int(input("Enter P:"))
        q = int(input("Enter Q:"))
        c = int(input("Enter Cipher:"))
        d = int(input("Enter Priv Key (D): "))
        print("Plaintext is: ", std_decrypt(c, p, q, d))
        input("\nPress Enter to continue...")
    elif x == 7:
        c = int(input("Enter Cipher: "))
        e = int(input("Enter Pub Key (E): \n(Make sure it's small)"))
        eth_root(c, e)
        input("\nPress Enter to continue...")
    elif x == 8:
        e = int(input("Enter BIG Pub Key:"))
        n = int(input("Enter N:"))
        print("Priv Key is:", owiener.attack(e, n))
        input("\nPress Enter to continue...")
    elif x == 0:
        quit()
    else:
        print("Bad input.")
