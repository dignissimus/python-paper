from paper import to_words, from_words

print(to_words([0x28, 0x67, 0x55, 0xfa, 0xd0, 0x48, 0x69, 0xca, 0x52, 0x33, 0x20, 0xac, 0xce, 0x0d, 0xc6, 0xa4]))
print(to_words(map(lambda x: ord(x), list("hello"))))
print(to_words(
    [0x87, 0x42, 0x8f, 0xc5, 0x22, 0x80, 0x3d, 0x31,
     0x06, 0x5e, 0x7b, 0xce, 0x3c, 0xf0, 0x3f, 0xe4,
     0x75, 0x09, 0x66, 0x31, 0xe5, 0xe0, 0x7b, 0xbd,
     0x7a, 0x0f, 0xde, 0x60, 0xc4, 0xcf, 0x25, 0xc7]))
print(to_words([0x1, 0x2, 0x0, 0xff]))
