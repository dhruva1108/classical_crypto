class dhruva_cipher:
    
    def __init__(self, key, plaintext = None, ciphertext = None):
        self.p = plaintext
        self.c = ciphertext
        self.k = key
        low = [[j + 26, chr(j + 97)] for j in range(26)]
        self.code = [[i, chr(i + 65)] for i in range(26)]
        for i in low:
            self.code.append(i)
        self.code.append([52, ' '])
        self.code.append([53, '.'])
        self.code.append([54, ','])
        self.code.append([55, ';'])
        self.code.append([56, ':'])
        self.code.append([57, '('])
        self.code.append([58, ')'])
        self.code.append([59, '"'])
        self.code.append([60, "'"])
        for i in range(10):
            self.code.append([60 + i + 1, f'{i}'])
        
    def encrypt(self):
        cipher = ''
        plain  = self.p
        for i in self.k:
            for j in self.code:
                if j[1] == i:
                    k_val = j[0]
                    break
            for m in plain:
                for j in self.code:
                    if j[1] == m:
                        m_val = j[0]
                        break
                val = (m_val + k_val) % len(self.code)
                for j in self.code:
                    if j[0] == val:
                        cipher += j[1]
            if i == self.k[-1]:
                break
            else:
                plain = cipher
                cipher = ''
        return cipher
    
    def decrypt(self, key):
        plain = ''
        cipher  = self.c
        if self.k == key:
            for i in self.k[::-1]:
                for j in self.code:
                    if j[1] == i:
                        k_val = j[0]
                        break
                for m in cipher:
                    for j in self.code:
                        if j[1] == m:
                            m_val = j[0]
                            break
                    val = (m_val - k_val) % len(self.code)
                    for j in self.code:
                        if j[0] == val:
                            plain += j[1]
                if i == self.k[0]:
                    break
                else:
                    cipher = plain
                    plain = ''
        else:
            return 'Please give correct key'
        return plain