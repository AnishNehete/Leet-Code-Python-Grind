class TimeMap:

    def __init__(self): #constructor
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]= [] #create an empty list for this key
        self.store[key].append([timestamp,value])    #append the new pair at the end because like problem guarantees that timestamps come in increasing order for each step

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        left = 0
        right = len(values)-1
        answer = ""

        while left <= right:
            mid = (left +right )//2 
            current_timestamp, current_value = values[mid]

            if current_timestamp <= timestamp:
                answer = current_value
                left = mid +1
            else:
                right = mid - 1

        return answer


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)