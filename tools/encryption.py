def xor_string(s1,s2):
    mul = int(len(s1) / len(s2)  + 1)
    s2 *= mul
    s2 = s2[:len(s1)]
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))