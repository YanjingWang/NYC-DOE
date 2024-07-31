class Complexity:

    def permutations(self,arr, start, end):
        if start == end:
            print(arr)
            return
    
        for i in range(start, end):
            arr[i], arr[start] = arr[start], arr[i]
            print("first interation i: ", i, "start: ", start, "end: ", end)
            self.permutations(arr, start + 1, end)
            arr[i], arr[start] = arr[start], arr[i]
            print("second iteration i: ", i, "start: ", start, "end: ", end)

if __name__ == "__main__":
    c = Complexity()
    c.permutations([1, 2, 3], 0, 3)

