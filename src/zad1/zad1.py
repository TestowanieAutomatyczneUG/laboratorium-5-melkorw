class Hamming():
    def distance(self, first, second):
        if first == '' and second == '':
            return 0
        if len(first) == 1 and len(second) == 1 and first == second:
            return 0
        if len(first) == 1 and len(second) == 1 and first != second:
            return 1



hamming  = Hamming()
print(hamming.distance('', ''))