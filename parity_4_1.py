'''
Parity brute-force iteratively test value and shift
Store number mod 2
time: O(n)
'''
def parityBF(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

'''
Parity better average using math
use k as the number of bits set to 1
time: O(k)
'''
def parityk(x):
    result = 0
    while x:
        result ^= 1
        x &= x -1 # this drops the LSB of x
    return result

'''
Parity but add caching for the same computation
use a lookup table
example for 2-bit words but write one for 16 bit words
def parityLT(x):
    mask_size = 16 # shift by 4
    bit_mask = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & bit_mask] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE)
                & bit_mask] ^ PRECOMPUTED_PARITY[x & bit_mask])
'''
def parityTB(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1



def main():
    for x in range(2):
        print(parityBF(x))
        print(parityk(x))
        print(parityTB(x))
    #    parityLT(11)

if __name__ == '__main__':
    main()

