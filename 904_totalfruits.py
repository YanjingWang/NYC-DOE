class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # sliding window
        # 1. find the longest subarray with at most 2 different numbers
        # 2. return the length of the subarray
        # 3. use a dictionary to store the number of each fruit
        # 4. use a variable to store the number of different fruits
        # 5. use two pointers to maintain the sliding window
        # 6. use a variable to store the maximum length
        # 7. use a while loop to iterate through the array
        # 8. use a while loop to move the right pointer until the number of different fruits is greater than 2
        # 9. use a while loop to move the left pointer until the number of different fruits is less than or equal to 2
        # 10. update the maximum length
        # 11. return the maximum length
        # Time complexity: O(n)
        # Space complexity: O(n)
        if not fruits:
            return 0
        fruit_dict = {}
        max_length = 0
        left = 0
        right = 0
        while right < len(fruits):
            fruit_dict[fruits[right]] = fruit_dict.get(fruits[right], 0) + 1
            while len(fruit_dict) > 2:
                fruit_dict[fruits[left]] -= 1
                if fruit_dict[fruits[left]] == 0:
                    del fruit_dict[fruits[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
    
if __name__ == "__main__":
    fruits = [1,2,1]
    print(Solution().totalFruit(fruits)) # 3
    
    fruits = [0,1,2,2]
    print(Solution().totalFruit(fruits)) # 3
    
    fruits = [1,2,3,2,2]
    print(Solution().totalFruit(fruits)) # 4
    
    fruits = [3,3,3,1,2,1,1,2,3,3,4]
    print(Solution().totalFruit(fruits)) # 5
    
    fruits = [0,1,6,6,4,4,6]
    print(Solution().totalFruit(fruits)) # 5