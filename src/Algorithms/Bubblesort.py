from typing import List, Any

class BubbleSort:
    def __init__(self, data: List[Any]):
        self.data = list(data)
        self.n = len(self.data)
    def sort(self) -> List[Any]:
        for i in range(self.n):
            swapped = False
            for j in range(0, self.n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    swapped = True
            if not swapped:
                break  
        return self.data

if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSort(unsorted_list)
    
    print(f"Lista original: {unsorted_list}")
    print(f"Lista ordenada: {sorter.sort()}")