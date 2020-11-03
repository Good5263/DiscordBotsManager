class Chiper:
    def shake(self, string):
        part1 = string[:len(string) // 2]
        part2 = string[len(string) // 2:]
        
        return ''.join([part1[i] + part2[i] for i in range(len(part1))])

    def reshake(self, string):
        part1 = [string[i] for i in range(0, len(string), 2)]
        part2 = [string[i] for i in range(1, len(string), 2)]

        return ''.join(part1 + part2)