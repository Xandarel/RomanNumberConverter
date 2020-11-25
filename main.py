class RomanNumberConverter:
    def __init__(self):
        self.converter = {'I': 1,
                          'V': 5,
                          'X': 10,
                          'L': 50,
                          'C': 100,
                          'D': 500,
                          'M': 1000}

    def romanToInt(self, s: str) -> int:
        main_sum = list()
        buffer = 0
        second_pos = True
        for element in s:
            if buffer == 0:
                buffer = self.converter[element]
                main_sum.append(buffer)
            else:
                if second_pos:
                    second_pos = False
                    if self.converter[element] > buffer:
                        main_sum[-1] = self.converter[element] - buffer
                        second_pos = True
                    buffer = self.converter[element]
                elif self.converter[element] > buffer:
                    main_sum.append(self.converter[element] - buffer)
                    second_pos = True
                else:
                    main_sum.append(buffer)
                    buffer = self.converter[element]
        if not second_pos:
            main_sum.append(buffer)
        res = sum(main_sum)
        if res < 4000:
            return res
        else:
            raise ValueError('заданное число выхлодит за диапазон работы программы')


converter = RomanNumberConverter()
print(converter.romanToInt('III'))
print(converter.romanToInt('IV'))
print(converter.romanToInt('IX'))
print(converter.romanToInt('LVIII'))
print(converter.romanToInt('MCMXCIV'))
print(converter.romanToInt('MMMCMXCIXI'))
