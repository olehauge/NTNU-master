from typing import List
from sage.all import *

# GOST R 34.12-2015: Block Cipher "Kuznyechik"

# Authors comment:
# Run it as a Python3 Jupiter Notebook.
#
# This program implements the decomposition of pi found in the "Reverse-Engineering the S-Box of Streebog, Kuznyechik
# and STRIBObr1" paper by Alex Biryukov, Leo Perrin, and Aleksei Udovenko; and adds it to the original code for the
# Kuznyechik provided for the second assignment task.
#
# Paper: https://eprint.iacr.org/2016/071.pdf
#
# The decomposition uses:
#   - A finite field defined by the polynomial X^4+X^3+1
#   - 4 non-linear 4-bit permutations
#   - A multiplicative inverse in the finite field
#   - 2 linear permutations.
#   - Finite filed multiplication (two times in the structure)
# We implement this functionality in order to evaluate the pi(l||r) as described by the authors:
#   1. (l||r) := a(l||r)
#   2. if r = 0 then l := v0(l), else l := v1(l*I(r))
#   3. r := o(r*phi(l))
#   4. return w(l||r)
#
# The result is an S-Box for pi.


# Defining the finite field based on the LFSR polynomial: X^4+X^3+1
X: int = GF(2).polynomial_ring().gen()
F = GF(2 ** 4, name="a", modulus=X ** 4 + X ** 3 + 1)


# Defining the field multiplication as seen in the decomposition (used twice)
def field_multiplication(x, y) -> int:
    return (F.fetch_int(x) * F.fetch_int(y)).integer_representation()


# Declaring the non-linear 4-bit functions identified by the authors
multiplicative_inv: List[int] = [(F.fetch_int(x) ** 14).integer_representation() for x in range(0, 16)]
nu_0: List[hex] = [0x2, 0x5, 0x3, 0xb, 0x6, 0x9, 0xe, 0xa, 0x0, 0x4, 0xf, 0x1, 0x8, 0xd, 0xc, 0x7]
nu_1: List[hex] = [0x7, 0x6, 0xc, 0x9, 0x0, 0xf, 0x8, 0x1, 0x4, 0x5, 0xb, 0xe, 0xd, 0x2, 0x3, 0xa]
phi: List[hex] = [0xb, 0x2, 0xb, 0x8, 0xc, 0x4, 0x1, 0xc, 0x6, 0x3, 0x5, 0x8, 0xe, 0x3, 0x6, 0xb]
sigma: List[hex] = [0xc, 0xd, 0x0, 0x4, 0x8, 0xb, 0xa, 0xe, 0x3, 0x9, 0x5, 0x2, 0xf, 0x1, 0x6, 0x7]


def linear_8_permutation(x, matrix) -> int:
    """
    Defining the linear 8-bit functions/permutations (used for alpha and omega)
    :param x: Takes the 4 bit right and left nibbles
    :param matrix: Takes alpha or omega as a matrix
    :return: Returns an integer value of the permutation
    """
    y = matrix * Matrix(GF(2), 8, 1, map(int, bin(x)[2:].zfill(8)))
    return int("".join(map(str, y.T[0][:8])), 2)


# Defining the matrix representation of the two linear permutations: alpha and omega
alpha = Matrix(GF(2), 8, 8, [
    0, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1,
    0, 1, 0, 0, 0, 0, 1, 1,
    1, 1, 1, 0, 1, 1, 1, 1,
    1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 0,
    0, 0, 0, 1, 1, 0, 1, 0,
    0, 0, 1, 0, 0, 0, 0, 0,
])

omega = Matrix(GF(2), 8, 8, [
    0, 0, 0, 0, 1, 0, 1, 0,
    0, 0, 0, 0, 0, 1, 0, 0,
    0, 0, 1, 0, 0, 0, 0, 0,
    1, 0, 0, 1, 1, 0, 1, 0,
    0, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 0,
    1, 0, 0, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1,
])


pi: List[int] = []
for l_II_r in range(256):
    """
    Computing pi using the decomposition and the evaluation described by the authors
    The for loop conducts the evaluation of pi(l||r) as described in the paper:
        (l||r) := a(l||r)
        if r = 0 then l := v0(l), else l := v1(l*I(r))
        r := o(r*phi(l))
        return w(l||r)
    :param l_II_r: Takes an integer value between 0 and 255
    :return: Returns pi
    """
    l_II_r: int = linear_8_permutation(l_II_r, alpha)
    l, r = l_II_r >> 4, l_II_r & 0xf
    l: int = (r == 0) * nu_0[l] + (r != 0) * nu_1[field_multiplication(l, multiplicative_inv[r])]
    r: int = sigma[field_multiplication(r, phi[l])]
    l_II_r: int = linear_8_permutation((l << 4) | r, omega)
    pi.append(l_II_r)

# The inverse of pi as described in RFC7801
pi_inverse: List[int] = [165, 45, 50, 143, 14, 48, 56, 192, 84, 230, 158, 57,
                         85, 126, 82, 145, 100, 3, 87, 90, 28, 96, 7, 24, 33,
                         114, 168, 209, 41, 198, 164, 63, 224, 39, 141, 12, 130,
                         234, 174, 180, 154, 99, 73, 229, 66, 228, 21, 183, 200,
                         6, 112, 157, 65, 117, 25, 201, 170, 252, 77, 191, 42,
                         115, 132, 213, 195, 175, 43, 134, 167, 177, 178, 91, 70,
                         211, 159, 253, 212, 15, 156, 47, 155, 67, 239, 217, 121,
                         182, 83, 127, 193, 240, 35, 231, 37, 94, 181, 30, 162,
                         223, 166, 254, 172, 34, 249, 226, 74, 188, 53, 202, 238,
                         120, 5, 107, 81, 225, 89, 163, 242, 113, 86, 17, 106, 137,
                         148, 101, 140, 187, 119, 60, 123, 40, 171, 210, 49, 222,
                         196, 95, 204, 207, 118, 44, 184, 216, 46, 54, 219, 105,
                         179, 20, 149, 190, 98, 161, 59, 22, 102, 233, 92, 108, 109,
                         173, 55, 97, 75, 185, 227, 186, 241, 160, 133, 131, 218,
                         71, 197, 176, 51, 250, 150, 111, 110, 194, 246, 80, 255,
                         93, 169, 142, 23, 27, 151, 125, 236, 88, 247, 31, 251, 124,
                         9, 13, 122, 103, 69, 135, 220, 232, 79, 29, 78, 4, 235,
                         248, 243, 62, 61, 189, 138, 136, 221, 205, 11, 19, 152, 2,
                         147, 128, 144, 208, 36, 52, 203, 237, 244, 206, 153, 16,
                         68, 64, 146, 58, 1, 38, 18, 16, 72, 104, 245, 129, 139, 199,
                         214, 32, 10, 8, 0, 76, 215, 116]


#
# 128-bits integer input and output
#
def substitution(a: int) -> int:
    """
    Defining the substitution function defined in RFC7801
    S:V_128-> V_128  S(a)=(a_15||...||a_0)=pi(a_15)||...||pi(a_0), where
      a_15||...||a_0 belongs to V_128, a_i belongs to V_8, i=0,1,...,15
    :param a: Takes an 128-bit integer as input
    :return: Returns an 128-bit integer
    """
    output: int = 0
    for i in reversed(range(16)):
        output <<= 8                            # Expose the 8 most significant bits of a
        output ^= pi[(a >> (8 * i)) & 0xff]     # Grab the 8 most significant bits of a. Used as input for the pi
    return output                               # Shifts output over by 8 positions and ajoin the next value of pi


def substitution_inverse(a: int) -> int:
    """
    Defining the inverse substitution as defined in RFC7801
    S^(-1):V_128-> V_128  S^(-1)(a_15||...||a_0)=pi^(-1) (a_15)||...||pi^(-1)(a_0), where
      a_15||...||a_0 belongs to V_128, a_i belongs to V_8, i=0,1,...,15
    :param a: Takes an 128-bit integer as input
    :return: Returns an 128-bit integer
    """
    output: int = 0
    for i in reversed(range(16)):
        output <<= 8                                # Same as for "substitution", but uses pi_inverse instead of pi
        output ^= pi_inverse[(a >> (8 * i)) & 0xff]
    return output


def binary_polynomial_multiplication(x: int, y: int) -> int:
    """
    Defining a part (1/3) of the ring residue modulo calculation
    :param x: Takes a non-negative integer
    :param y: Takes a non-negative integer
    :return: Retruns a binary representation of the polynomial
    """
    if x == 0 or y == 0:
        return 0
    z: int = 0
    while x != 0:
        if x & 1 == 1:
            z ^= y
        y <<= 1
        x >>= 1
    return z


def number_of_bits_in_polynomial(binary_polynomial: int) -> int:
    """
    Defining a part (2/3) of the ring residue modulo calculation
    :param binary_polynomial: The input is a binary representation of the polynomial
    :return: Returns an integer value of the number of bits in the polynomial
    """
    if binary_polynomial == 0:
        return 0
    number_of_bits: int = 0
    while binary_polynomial != 0:
        number_of_bits += 1
        binary_polynomial >>= 1
    return number_of_bits


def polynomial_integer_modulo(x: int, p: int) -> int:
    """
    Defining a part (3/3) of the ring residue modulo calculation
    Z_(2^n) ring of residues modulo 2^n
    :param x: Takes a non-negative integer as input
    :param p: Takes a non-negative integer as input
    :return: Returns the modulo value of the polynomials
    """
    number_of_bits_p: int = number_of_bits_in_polynomial(p)
    while True:
        number_of_bits_x = number_of_bits_in_polynomial(x)
        if number_of_bits_x < number_of_bits_p:
            return x
        m_shift: int = p << (number_of_bits_x - number_of_bits_p)
        x ^= m_shift


def delta_bijective_mapping(x: int, y: int) -> int:
    """
    Defining the bijective mapping as described in RFC7801
    delta: V_8 -> Q  bijective mapping that maps a binary string from V_8
           into an element from field Q as follows: string
           z_7||...||z_1||z_0, where z_i in {0, 1}, i = 0, ..., 7,
           corresponds to the element z_0+(z_1*theta)+...+(z_7*theta^7)
           belonging to Z
    :param x: Takes an 8-bit integer as input
    :param y: Takes an 8-bit integer as input
    :return: Returns an integer value as result of the bijective mapping
    """
    multiplied_polynomial: int = binary_polynomial_multiplication(x, y)
    p = int('111000011', 2)     # p(x)=x^8+x^7+x^6+x+1
    return polynomial_integer_modulo(multiplied_polynomial, p)


def linear_transformation(x: int) -> int:
    """
    Defining the linear transformation as described in RFC7801
    l: (V_8)^16 -> V_8: l(a_15,...,a_0) = nabla(148*delta(a_15) + 32*delta(a_15) +
     133*delta(a_13) + 16*delta(a_12) + 194*delta(a_11) +
     192*delta(a_10) + 1*delta(a_9) + 251*delta(a_8) + 1*delta(a_7) +
     192*delta(a_6) + 194*delta(a_5) + 16*delta(a_4) + 133*delta(a_3) +
     32*delta(a_2) + 148*delta(a_1) +1*delta(a_0))
    :param x: The input is a vector of 16 8-bits values (128-bits)
    :return: Returns an 8-bit integer value
    """
    constants: List[int] = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]
    output: int = 0
    while x != 0:
        output ^= delta_bijective_mapping(x & 0xff, constants.pop())
        x >>= 8
    return output


def transformation_R(x: int) -> int:
    """
    Defining the transformation R as described in RFC7801
     R:V_128-> V_128  R(a_15||...||a_0)=l(a_15,...,a_0)||a_15||...||a_1,
      where a_15||...||a_0 belongs to V_128, a_i belongs to V_8,
      i=0,1,...,15
    :param x: Takes an 128-bit integer value
    :return: Returns an 128-bit integer value
    """
    a: int = linear_transformation(x)
    return (a << 8 * 15) ^ (x >> 8)


def inverse_transformation_R(x: int) -> int:
    """
    Defining the inverse transformation R as described in RFC7801
    R^(-1):V_128-> V_128  the inverse transformation of R, which may be
      calculated, for example, as follows: R^(-1)(a_15||...||a_0)=a_14||
      a_13||...||a_0||l(a_14,a_13,...,a_0,a_15), where a_15||...||a_0
      belongs to V_128, a_i belongs to V_8, i=0,1,...,15
    :param x: Takes an 128-bit integer value
    :return: Returns an 128-bit integer value
    """
    a: int = x >> 8 * 15
    x: int = x << 8 & (2 ** 128 - 1)
    b: int = linear_transformation(x ^ a)
    return x ^ b


def transformation_L(x: int) -> int:
    """
    Defining the transformation L as described in RFC7801
    L:V_128-> V_128  L(a)=R^(16)(a), where a belongs to V_128
    :param x: Takes 128-bit integer as input
    :return: Returns 128-bit integer
    """
    for _ in range(16):
        x = transformation_R(x)
    return x


def inverse_transformation_L(x: int) -> int:
    """
    Defining the inverse transformation L as described in RFC7801
    L^(-1):V_128-> V_128  L^(-1)(a)=(R^(-1))(16)(a), where a belongs to
      V_128
    :param x: Takes 128-bit integer as input
    :return: Returns 128-bit integer
    """
    for _ in range(16):
        x = inverse_transformation_R(x)
    return x


def key_schedule(key: int) -> List:
    """
    Defining the key schedule as described in RFC7801
    Key schedule uses round constants C_i belonging to V_128, i=1, 2,
    ..., 32, defined as

    C_i=L(Vec_128(i)), i=1,2,...,32.

    Round keys K_i, i=1, 2, ..., 10 are derived from key
    K=k_255||...||k_0 belonging to V_256, k_i belongs to V_1, i=0, 1,
    ..., 255, as follows:

    K_1=k_255||...||k_128;
    K_2=k_127||...||k_0;
    (K_(2i+1),K_(2i+2))=F[C_(8(i-1)+8)]...
     F[C_(8(i-1)+1)](K_(2i-1),K_(2i)), i=1,2,3,4.
    :param key: Takes a 256-bit input
    :return: Returns 10 128-bit round keys
    """
    round_keys: List[int] = []
    round_key_1: int = key >> 128
    round_key_2: int = key & (2 ** 128 - 1)
    round_keys.append(round_key_1)
    round_keys.append(round_key_2)
    for i in range(4):
        for j in range(8):
            c: int = transformation_L(8 * i + j + 1)  # The line below: F[k](a_1,a_0)=(LSX[k](a_1)(xor)a_0,a_1)
            (round_key_1, round_key_2) = (transformation_L(substitution(round_key_1 ^ c)) ^ round_key_2, round_key_1)
        round_keys.append(round_key_1)
        round_keys.append(round_key_2)
    return round_keys


def encipherment(plaintext: int, key: int) -> int:
    """
    Defining the encipherment algorithm as described in RFC7801
    E_(K_1,...,K_10)(a)=X[K_10]LSX[K_9]...LSX[K_2]LSX[K_1](a),
     where a belongs to V_128.
    :param plaintext: Takes a 128-bit integer plaintext value
    :param key: Takes a 256-bit integer key value
    :return: Returns a 128-bit integer ciphertext value
    """
    keys: List[int] = key_schedule(key)
    for round in range(9):
        plaintext = transformation_L(substitution(plaintext ^ keys[round]))
    return plaintext ^ keys[-1]


def decipherment(ciphertext: int, key: int) -> int:
    """
    Defining the decipherment algorithm as described in RFC7801
    D_(K_1,...,K_10)(a)=X[K_1]L^(-1)S^(-1)X[K_2]...
     L^(-1)S^(-1)X[K_9] L^(-1)S^(-1)X[K_10](a),
    where a belongs to V_128.
    :param ciphertext: Takes a 128-bit integer ciphertext value
    :param key: Takes a 256-bit integer key value
    :return: Returns a 128-bit integer plaintext value
    """
    keys: List[int] = key_schedule(key)
    keys.reverse()
    for round in range(9):
        ciphertext = substitution_inverse(inverse_transformation_L(ciphertext ^ keys[round]))
    return ciphertext ^ keys[-1]


def test_code(key_value: str, plain_text: str, cipher_text: str):
    """
    Testing the code against the tests declared by the assignment (5.4, 5.5, and 5.6)
    :param key_value: The 256-bit integer key value to be tested
    :param plain_text: The 128-bit integer plaintext value to be tested
    :param cipher_text: The 128-bit ciphertext value to be tested
    :return: This function only prints the results to the terminal
    """
    # Test subsection 5.4 in RFC7801
    key = int(key_value, 16)
    print('=======================================')
    print('Key schedule test results:')
    i = 0
    for round_key in key_schedule(key):
        i += 1
        print('K_' + str(i) + ' = ' + hex(round_key))
    print('\nExpected results:\n'
          'K_1 = 8899aabbccddeeff0011223344556677\n'
          'K_2 = fedcba98765432100123456789abcdef\n'
          'K_3 = db31485315694343228d6aef8cc78c44\n'
          'K_4 = 3d4553d8e9cfec6815ebadc40a9ffd04\n'
          'K_5 = 57646468c44a5e28d3e59246f429f1ac\n'
          'K_6 = bd079435165c6432b532e82834da581b\n'
          'K_7 = 51e640757e8745de705727265a0098b1\n'
          'K_8 = 5a7925017b9fdd3ed72a91a22286f984\n'
          'K_9 = bb44e25378c73123a5f32f73cdb6e517\n'
          'K_10 = 72e9dd7416bcf45b755dbaa88e4a4043\n')

    # Test subsection 5.5 in RFC7801
    a = int(plain_text, 16)
    b = encipherment(a, key)
    print('=======================================')
    print('Encipherment test result:')
    print('b = ' + hex(b))
    print('\nExpected results:\n'
          'b = 7f679d90bebc24305a468d42b9d4edcd\n')

    # Test subsection 5.6 in RFC7801
    b = int(cipher_text, 16)
    a = decipherment(b, key)
    print('=======================================')
    print('Decipherment test result:')
    print('b = ' + hex(a))
    print('\nExpected results:\n'
          'a = 1122334455667700ffeeddccbbaa9988')

 
# Supply key value, plaintext value, and ciphertext value as string
test_code('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef', '1122334455667700ffeeddccbbaa9988',
          '7f679d90bebc24305a468d42b9d4edcd')
