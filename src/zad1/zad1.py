class Hamming():
    def distance(self, first, second):
        if len(first) != len(second):
            raise ValueError('Values can\'t be different length')

        if len(first) == len(second) and first == second:
            return 0

        if len(first) == len(second) and first != second:
            wyn = 0
            for i in range(0, len(first)):
                if first[i] != second[i]:
                    wyn += 1
            return wyn



hamming  = Hamming()
