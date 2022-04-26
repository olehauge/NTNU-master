from typing import List

# Author: Ole Andre Hauge (538916)
# Authors comment:
#
# This is an implementation of GOST R 34.12-2015: Block Cipher "Kuznyechik"
# This program implements the Kuznyechik block cipher as it is described in RFC7801
# RFC source: https://tools.ietf.org/pdf/rfc7801.pdf


# The pi S-box and inverse of pi as defined in RFC7801
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


def substitution(xor_result: int) -> int:
    """
    Defining the substitution function defined in RFC7801
    S:V_128-> V_128  S(a)=(a_15||...||a_0)=pi(a_15)||...||pi(a_0), where
      a_15||...||a_0 belongs to V_128, a_i belongs to V_8, i=0,1,...,15
    :param xor_result: Takes an 128-bit integer as input stemming from the plaintext XORed with a round key
    :return: Returns an 128-bit integer
    """
    output: int = 0
    for i in reversed(range(16)):
        output <<= 8                                  # Expose the 8 most significant bits of a
        output ^= pi[(xor_result >> (8 * i)) & 0xff]  # Grab the 8 most significant bits of a. Used as input for the pi
    return output                                     # Shifts output over by 8 positions and ajoin the next value of pi


def substitution_inverse(inv_trans_result: int) -> int:
    """
    Defining the inverse substitution as defined in RFC7801
    S^(-1):V_128-> V_128  S^(-1)(a_15||...||a_0)=pi^(-1) (a_15)||...||pi^(-1)(a_0), where
      a_15||...||a_0 belongs to V_128, a_i belongs to V_8, i=0,1,...,15
    :param inv_trans_result: Takes an 128-bit integer as input stemming from the return value of the
    inverse_transformation_L() function
    :return: Returns an 128-bit integer
    """
    output: int = 0
    for i in reversed(range(16)):
        output <<= 8    # Same as for "substitution", but uses pi_inverse instead of pi
        output ^= pi_inverse[(inv_trans_result >> (8 * i)) & 0xff]
    return output


def polynomial_binary_multiplication(vector_8b: int, bijective_constant: int) -> int:
    """
    Defining a part (1/3) of the ring residue modulo calculation
    :param vector_8b: Takes a non-negative integer
    :param bijective_constant: Takes a non-negative integer
    :return: Returns a binary representation of the polynomial
    """
    if vector_8b == 0 or bijective_constant == 0:
        return 0
    output: int = 0
    while vector_8b != 0:
        if vector_8b & 1 == 1:
            output ^= bijective_constant
        bijective_constant <<= 1
        vector_8b >>= 1
    return output


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


def polynomial_integer_modulo(multiplied_polynomial: int, polynomial_binary: int) -> int:
    """
    Defining a part (3/3) of the ring residue modulo calculation
    Z_(2^n) ring of residues modulo 2^n
    :param multiplied_polynomial: Takes a non-negative integer as input resulting from a
    binary polynomial multiplication
    :param polynomial_binary: Takes a non-negative integer as input representing the polynomial of the field
    :return: Returns the modulo value of the polynomials
    """
    number_of_bits_p: int = number_of_bits_in_polynomial(polynomial_binary)
    while True:
        number_of_bits_x = number_of_bits_in_polynomial(multiplied_polynomial)
        if number_of_bits_x < number_of_bits_p:
            return multiplied_polynomial
        m_shift: int = polynomial_binary << (number_of_bits_x - number_of_bits_p)
        multiplied_polynomial ^= m_shift


def delta_bijective_mapping(vector_8b: int, bijective_constant: int) -> int:
    """
    Defining the bijective mapping as described in RFC7801
    delta: V_8 -> Q  bijective mapping that maps a binary string from V_8
           into an element from field Q as follows: string
           z_7||...||z_1||z_0, where z_i in {0, 1}, i = 0, ..., 7,
           corresponds to the element z_0+(z_1*theta)+...+(z_7*theta^7)
           belonging to Z
    :param vector_8b: Takes an 8-bit integer as input resulting from one of the 16 8-bits values
    from the linear_transformation function
    :param bijective_constant: Takes an 8-bit integer as input from the constant list in the
    linear_transformation function
    :return: Returns an integer value as result of the bijective mapping
    """
    multiplied_polynomial: int = polynomial_binary_multiplication(vector_8b, bijective_constant)
    polynomial_binary = int('111000011', 2)     # p(x)=x^8+x^7+x^6+x+1
    return polynomial_integer_modulo(multiplied_polynomial, polynomial_binary)


def linear_transformation(vector: int) -> int:
    """
    Defining the linear transformation as described in RFC7801
    l: (V_8)^16 -> V_8: l(a_15,...,a_0) = nabla(148*delta(a_15) + 32*delta(a_15) +
     133*delta(a_13) + 16*delta(a_12) + 194*delta(a_11) +
     192*delta(a_10) + 1*delta(a_9) + 251*delta(a_8) + 1*delta(a_7) +
     192*delta(a_6) + 194*delta(a_5) + 16*delta(a_4) + 133*delta(a_3) +
     32*delta(a_2) + 148*delta(a_1) +1*delta(a_0))
    :param vector: The input is a vector of 16 8-bits values (128-bits)
    :return: Returns an 8-bit integer value
    """
    constants: List[int] = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]
    output: int = 0
    while vector != 0:
        output ^= delta_bijective_mapping(vector & 0xff, constants.pop())
        vector >>= 8
    return output


def transformation_R(sub_result: int) -> int:
    """
    Defining the transformation R as described in RFC7801
     R:V_128-> V_128  R(a_15||...||a_0)=l(a_15,...,a_0)||a_15||...||a_1,
      where a_15||...||a_0 belongs to V_128, a_i belongs to V_8,
      i=0,1,...,15
    :param sub_result: Takes 128-bit integer as input stemming from the return value of the substitution function
    :return: Returns an 128-bit integer value
    """
    byte_transformed: int = linear_transformation(sub_result)
    return (byte_transformed << 8 * 15) ^ (sub_result >> 8)


def inverse_transformation_R(xor_result: int) -> int:
    """
    Defining the inverse transformation R as described in RFC7801
    R^(-1):V_128-> V_128  the inverse transformation of R, which may be
      calculated, for example, as follows: R^(-1)(a_15||...||a_0)=a_14||
      a_13||...||a_0||l(a_14,a_13,...,a_0,a_15), where a_15||...||a_0
      belongs to V_128, a_i belongs to V_8, i=0,1,...,15
    :param xor_result: Takes an 128-bit integer value resulting from the ciphertext XORed with a round key
    :return: Returns an 128-bit integer value
    """
    byte_i: int = xor_result >> 8 * 15
    xor_result: int = xor_result << 8 & (2 ** 128 - 1)
    byte_transformed: int = linear_transformation(xor_result ^ byte_i)
    return xor_result ^ byte_transformed


def transformation_L(sub_result: int) -> int:
    """
    Defining the transformation L as described in RFC7801
    L:V_128-> V_128  L(a)=R^(16)(a), where a belongs to V_128
    :param sub_result: Takes 128-bit integer as input stemming from the return value of the substitution function
    :return: Returns 128-bit integer
    """
    for _ in range(16):
        sub_result = transformation_R(sub_result)
    return sub_result


def inverse_transformation_L(xor_result: int) -> int:
    """
    Defining the inverse transformation L as described in RFC7801
    L^(-1):V_128-> V_128  L^(-1)(a)=(R^(-1))(16)(a), where a belongs to
      V_128
    :param xor_result: Takes 128-bit integer as input resulting from the ciphertext XORed with a round key
    :return: Returns 128-bit integer
    """
    for _ in range(16):
        xor_result = inverse_transformation_R(xor_result)
    return xor_result


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
            transform_result: int = transformation_L(8 * i + j + 1)     # F[k](a_1,a_0)=(LSX[k](a_1)(xor)a_0,a_1)
            (round_key_1, round_key_2) = (transformation_L(
                substitution(round_key_1 ^ transform_result)) ^ round_key_2, round_key_1)
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
    print('========================================')
    print('Key schedule test results:')
    i = 0
    for round_key in key_schedule(key):
        i += 1
        print('K_' + str(i) + ' = ' + hex(round_key))
    print('\nExpected results:\n'
          'K_1 = 0x8899aabbccddeeff0011223344556677\n'
          'K_2 = 0xfedcba98765432100123456789abcdef\n'
          'K_3 = 0xdb31485315694343228d6aef8cc78c44\n'
          'K_4 = 0x3d4553d8e9cfec6815ebadc40a9ffd04\n'
          'K_5 = 0x57646468c44a5e28d3e59246f429f1ac\n'
          'K_6 = 0xbd079435165c6432b532e82834da581b\n'
          'K_7 = 0x51e640757e8745de705727265a0098b1\n'
          'K_8 = 0x5a7925017b9fdd3ed72a91a22286f984\n'
          'K_9 = 0xbb44e25378c73123a5f32f73cdb6e517\n'
          'K_10 = 0x72e9dd7416bcf45b755dbaa88e4a4043\n')

    # Test subsection 5.5 in RFC7801
    plaintext = int(plain_text, 16)
    ciphertext = encipherment(plaintext, key)
    print('========================================')
    print('Encipherment test result:')
    print('b = ' + hex(ciphertext))
    print('\nExpected results:\n'
          'b = 0x7f679d90bebc24305a468d42b9d4edcd\n')

    # Test subsection 5.6 in RFC7801
    ciphertext = int(cipher_text, 16)
    plaintext = decipherment(ciphertext, key)
    print('========================================')
    print('Decipherment test result:')
    print('b = ' + hex(plaintext))
    print('\nExpected results:\n'
          'a = 0x1122334455667700ffeeddccbbaa9988')


if __name__ == '__main__':
    # Supply key value, plaintext value, and ciphertext value as string
    test_code('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef', '1122334455667700ffeeddccbbaa9988',
              '7f679d90bebc24305a468d42b9d4edcd')
