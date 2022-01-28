# GOST R 34.12-2015: Block Cipher "Kuznyechik"

# Functions
from typing import List

pi: List[int] = [252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35,
      197, 4, 77, 233, 119, 240, 219, 147, 46, 153, 186, 23, 54,
      241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239,
      33, 129, 28, 60, 66, 139, 1, 142, 79, 5, 132, 2, 174, 227,
      106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52,
      44, 81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206,
      204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156,
      183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145,
      120, 111, 157, 158, 178, 177, 50, 117, 25, 61, 255, 53, 138,
      126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169,
      62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224,
      15, 236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51,
      10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130,
      100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163,
      165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172, 29,
      247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73,
      76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133, 97, 32,
      113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229,
      108, 82, 89, 166, 116, 210, 230, 244, 180, 192, 209, 102,
      175, 194, 57, 75, 99, 182]

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


def S(a: int) -> int:
    """
    S:V_128-> V_128  S(a)=(a_15||...||a_0)=pi(a_15)||...||pi(a_0), where
      a_15||...||a_0 belongs to V_128, a_i belongs to V_8, i=0,1,...,15,

    a = 128-bit integer
    output = 128-bit integer

    :param a:
    :return output:
    """

    output: int = 0
    for i in reversed(range(16)):            # Start from 15 and go to 0
        output <<= 8                         # In the first cycle of the loop when i = 15, a shifts over by 120 positions "a >> (15 * 8)" to expose the 8 most significant bits of a
        output ^= pi[(a >> (8 * i)) & 0xff]  # a is and'ed with 0xff (eight 1's) which grabs the 8 most significant bits of a, which is used as input for the s-box "pi"
    return output                            # and ajoin that to the value of o. Each loop shifts o over by 8 positions and ajoin the next value of pi.


def S_inverse(a: int) -> int:
    """
    S^(-1):V_128-> V_128  the inverse transformation of S, which may be
      calculated, for example, as follows:
      S^(-1)(a_15||...||a_0)=pi^(-1) (a_15)||...||pi^(-1)(a_0), where
      a_15||...||a_0 belongs to V_128, a_i belongs to V_8, i=0,1,...,15,

    a = 128-bit integer
    output = 128-bit integer

    :param a:
    :return output:
    """
    output: int = 0
    for i in reversed(range(16)):
        output <<= 8
        output ^= pi_inverse[(a >> (8 * i)) & 0xff]
    return output


# TODO: Z_(2^n) ring of residues modulo 2^n part 1 / 3
# x and y are non-negative integers
# Their associated binary polynomials are multiplied.
# The associated integer to this product is returned.
def Z_polynomial_multiplication(x: int, y: int) -> int:
    """
    Z_(2^n) ring of residues modulo 2^n

    Vec_s: Z_(2^s) -> V_s  bijective mapping that maps an element from
           ring Z_(2^s) into its binary representation, i.e., for an
           element z of the ring Z_(2^s), represented by the residue z_0
           + (2*z_1) + ... + (2^(s-1)*z_(s-1)), where z_i in {0, 1}, i =
           0, ..., n-1, the equality Vec_s(z) = z_(s-1)||...||z_1||z_0
           holds

    :param x:
    :param y:
    :return z:
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


# TODO: Z_(2^n) ring of residues modulo 2^n part 2 / 3
# Returns the number of bits used to store the non-negative integer x
def z_get_number_of_bits(x: int) -> int:
    """
    Z_(2^n) ring of residues modulo 2^n

    Vec_s: Z_(2^s) -> V_s  bijective mapping that maps an element from
           ring Z_(2^s) into its binary representation, i.e., for an
           element z of the ring Z_(2^s), represented by the residue z_0
           + (2*z_1) + ... + (2^(s-1)*z_(s-1)), where z_i in {0, 1}, i =
           0, ..., n-1, the equality Vec_s(z) = z_(s-1)||...||z_1||z_0
           holds

    :param x:
    :return number_of_bits:
    """
    if x == 0:
        return 0
    number_of_bits: int = 0
    while x != 0:
        number_of_bits += 1
        x >>= 1
    return number_of_bits


# TODO: Z_(2^n) ring of residues modulo 2^n part 3 / 3
# x is a non-negative integer
# p is a positive integer
def z_mod_int_as_polynomial(x: int, p: int) -> int:
    """
    Z_(2^n) ring of residues modulo 2^n

    Vec_s: Z_(2^s) -> V_s  bijective mapping that maps an element from
           ring Z_(2^s) into its binary representation, i.e., for an
           element z of the ring Z_(2^s), represented by the residue z_0
           + (2*z_1) + ... + (2^(s-1)*z_(s-1)), where z_i in {0, 1}, i =
           0, ..., n-1, the equality Vec_s(z) = z_(s-1)||...||z_1||z_0
           holds

    :param x:
    :param p:
    :return x:
    """
    number_of_bits_p: int = z_get_number_of_bits(p)
    while True:
        number_of_bits_x = z_get_number_of_bits(x)
        if number_of_bits_x < number_of_bits_p:
            return x
        m_shift: int = p << (number_of_bits_x - number_of_bits_p)
        x ^= m_shift


# TODO: delta  V_8 -> Q  bijective mapping that maps a binary string from V_8
# into an element from field Q as follows:
# strings z_7||...||z_1||z_0, where z_i in {0, 1}, i = 0, ..., 7,
# corresponds to the element z_0+(z_1*theta)+...+(z_7*theta^7) belonging to Z,
# x, y are 8 bits
# The output is an 8 bit value
def delta(x: int, y: int) -> int:
    """
    delta: V_8 -> Q  bijective mapping that maps a binary string from V_8
           into an element from field Q as follows: string
           z_7||...||z_1||z_0, where z_i in {0, 1}, i = 0, ..., 7,
           corresponds to the element z_0+(z_1*theta)+...+(z_7*theta^7)
           belonging to Z,

    :param x:
    :param y:
    :return z_mod_int_as_polynomial(z_polynomial, p):
    """
    z_polynomial: int = Z_polynomial_multiplication(x, y)
    p = int('111000011', 2)                              # p(x)=x^8+x^7+x^6+x+1
    return z_mod_int_as_polynomial(z_polynomial, p)


# TODO: Linear Transformation --> l: (V_8)^16 -> V_8
# The input x is 128 bits (considered as a vector of 16 bytes)
# The return value is 8 bits
def l(x: int) -> int:
    """
    The linear transformation is denoted by l: (V_8)^16 -> V_8, and
    defined as:

    l(a_15,...,a_0) = nabla(148*delta(a_15) + 32*delta(a_15) +
    133*delta(a_13) + 16*delta(a_12) + 194*delta(a_11) +
    192*delta(a_10) + 1*delta(a_9) + 251*delta(a_8) + 1*delta(a_7) +
    192*delta(a_6) + 194*delta(a_5) + 16*delta(a_4) + 133*delta(a_3) +
    32*delta(a_2) + 148*delta(a_1) +1*delta(a_0)),

    for all a_i belonging to V_8, i = 0, 1, ..., 15, where the addition
    and multiplication operations are in the field Q, and constants are
    elements of the field as defined above.

    :param x:
    :return output:
    """
    constants: List[int] = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]
    output: int = 0
    while x != 0:
        output ^= delta(x & 0xff, constants.pop())
        x >>= 8
    return output


# TODO: R:V_128-> V_128  R(a_15||...||a_0)=l(a_15,...,a_0)||a_15||...||a_1, where a_15||...||a_0 belongs
# to V_128, a_i belongs to V_8, i=0,1,...,15,
# The input value x and output are 128-bits
def R(x: int) -> int:
    """
    R:V_128-> V_128  R(a_15||...||a_0)=l(a_15,...,a_0)||a_15||...||a_1,
      where a_15||...||a_0 belongs to V_128, a_i belongs to V_8,
      i=0,1,...,15,

    :param x:
    :return (a << 8 * 15) ^ (x >> 8):
    """
    a: int = l(x)
    return (a << 8 * 15) ^ (x >> 8)


# TODO: R^(-1):V_128-> V_128  the inverse transformation of R,
# which may be calculated, for example, as follows:
# R^(-1)(a_15||...||a_0)=a_14|| a_13||...||a_0||l(a_14,a_13,...,a_0,a_15),
# where a_15||...||a_0 belongs to V_128, a_i belongs to V_8, i=0,1,...,15,
def R_inverse(x: int) -> int:
    """
    R^(-1):V_128-> V_128  the inverse transformation of R, which may be
      calculated, for example, as follows: R^(-1)(a_15||...||a_0)=a_14||
      a_13||...||a_0||l(a_14,a_13,...,a_0,a_15), where a_15||...||a_0
      belongs to V_128, a_i belongs to V_8, i=0,1,...,15,

    :param x:
    :return x ^ b:
    """
    a: int = x >> 8 * 15
    x: int = x << 8 & (2 ** 128 - 1)
    b: int = l(x ^ a)
    return x ^ b


# TODO: L:V_128-> V_128  L(a)=R^(16)(a), where a belongs to V_128,
# The input value x and output value are 128-bits
# This function is the composition of R 16 times
def L(x: int) -> int:
    """
    L:V_128-> V_128  L(a)=R^(16)(a), where a belongs to V_128,

    :param x:
    :return x:
    """
    for _ in range(16):
        x = R(x)
    return x


# TODO: L^(-1):V_128-> V_128  L^(-1)(a)=(R^(-1))(16)(a), where a belongs to V_128, and
# The input value x and output value are 128-bits
# This function is the composition of R_inverse 16 times
def L_inverse(x: int) -> int:
    """
    L^(-1):V_128-> V_128  L^(-1)(a)=(R^(-1))(16)(a), where a belongs to V_128

    :param x:
    :return x:
    """
    for _ in range(16):
        x = R_inverse(x)
    return x


# TODO: F[k]:V_128[*]V_128 -> V_128[*]V_128 F[k](a_1,a_0)=(LSX[k](a_1)(xor)a_0,a_1),
# where k, a_0, a_1 belong to V_128.


# TODO: Key Schedule
# K is a 256-bit value
# The key schedule returns 10 keys of 128 bits each
def key_schedule(K: int) -> List:
    """
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

    :param K:
    :return keys:
    """
    keys: List[int] = []
    k_1: int = K >> 128
    k_2: int = K & (2 ** 128 - 1)
    keys.append(k_1)
    keys.append(k_2)
    for i in range(4):
        for j in range(8):
            c: int = L(8 * i + j + 1)
            (k_1, k_2) = (L(S(k_1 ^ c)) ^ k_2, k_1)     # <-- F[k](a_1,a_0)=(LSX[k](a_1)(xor)a_0,a_1)
        keys.append(k_1)
        keys.append(k_2)
    return keys


# TODO: Encryption
# Depending on the values of round keys K_1,...,K_10, the encryption
#    algorithm is a substitution E_(K_1,...,K_10) defined as follows:
#
#    E_(K_1,...,K_10)(a)=X[K_10]LSX[K_9]...LSX[K_2]LSX[K_1](a),
#
#    where a belongs to V_128.
# The plaintext x is 128 bits
# The key K is 256 bits
def encipherment(x: int, K: int) -> int:
    """
    Depending on the values of round keys K_1,...,K_10, the encryption
    algorithm is a substitution E_(K_1,...,K_10) defined as follows:

    E_(K_1,...,K_10)(a)=X[K_10]LSX[K_9]...LSX[K_2]LSX[K_1](a),
    where a belongs to V_128

    :param x:
    :param K:
    :return x ^ keys[-1]:
    """
    keys: List[int] = key_schedule(K)
    for round in range(9):
        x = L(S(x ^ keys[round]))
    return x ^ keys[-1]


# TODO: Decryption
# Depending on the values of round keys K_1,...,K_10, the decryption
#    algorithm is a substitution D_(K_1,...,K_10) defined as follows:
#
#    D_(K_1,...,K_10)(a)=X[K_1]L^(-1)S^(-1)X[K_2]...
#     L^(-1)S^(-1)X[K_9] L^(-1)S^(-1)X[K_10](a),
#
#    where a belongs to V_128.
#  The plaintext x is 128 bits
#  The key K is 256 bits
def decipherment(x: int, K: int) -> int:
    """
    Depending on the values of round keys K_1,...,K_10, the decryption
    algorithm is a substitution D_(K_1,...,K_10) defined as follows:

    D_(K_1,...,K_10)(a)=X[K_1]L^(-1)S^(-1)X[K_2]...
     L^(-1)S^(-1)X[K_9] L^(-1)S^(-1)X[K_10](a),
    where a belongs to V_128.

    :param x:
    :param K:
    :return x ^ keys[-1]:
    """
    keys: List[int] = key_schedule(K)
    keys.reverse()
    for round in range(9):
        x = S_inverse(L_inverse(x ^ keys[round]))
    return x ^ keys[-1]


if __name__ == '__main__':
    K = int('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef', 16)
    x = int('1122334455667700ffeeddccbbaa9988', 16)
    ciphertext = encipherment(x, K)
    decrypted_text = decipherment(ciphertext, K)
    print(hex((decrypted_text)))