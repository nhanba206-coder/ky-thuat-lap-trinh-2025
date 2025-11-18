class RomanConverter:
    def __init__(self):
        self.map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def roman_to_int(self, s):
        s = s.upper()
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and self.map.get(s[i], 0) < self.map.get(s[i+1], 0):
                total += self.map[s[i+1]] - self.map[s[i]]
                i += 2
            else:
                total += self.map.get(s[i], 0)
                i += 1
        return total

rc = RomanConverter()
print(rc.roman_to_int("III"))    
print(rc.roman_to_int("IX"))      
print(rc.roman_to_int("MMXXV"))   
