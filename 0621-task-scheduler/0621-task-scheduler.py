from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)

        #count how many times each tasks appear example {'a','a','a', 'b'} -> {'A':3,'B':3}
        freq = Counter(tasks)


        max_freq = max(freq.values())
        count_max = 0
        for count in freq.values():
            if count == max_freq:
                count_max +=1

        part_count = max_freq - 1
        part_length = n + 1
        candidate = part_count * part_length + count_max
        return max(len(tasks), candidate)



