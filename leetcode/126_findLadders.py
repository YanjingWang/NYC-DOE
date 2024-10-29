#leetcode 126.
# 126. Word Ladder II
# Hard
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
            
            # # build a graph
            # # bfs to find the shortest path
            # # dfs to find all the paths
            
            # # build a graph
            # wordList = set(wordList)
            # if endWord not in wordList:
            #     return []
            
            # graph = collections.defaultdict(list)
            # for word in wordList:
            #     for i in range(len(word)):
            #         graph[word[:i] + "*" + word[i+1:]].append(word)
            
            # # bfs to find the shortest path
            # queue = collections.deque()
            # queue.append((beginWord, [beginWord]))
            # visited = set()
            # visited.add(beginWord)
            # found = False
            # while queue and not found:
            #     size = len(queue)
            #     for _ in range(size):
            #         word, path = queue.popleft()
            #         if word == endWord:
            #             found = True
            #             break
            #         for i in range(len(word)):
            #             for next_word in graph[word[:i] + "*" + word[i+1:]]:
            #                 if next_word not in visited:
            #                     visited.add(next_word)
            #                     queue.append((next_word, path + [next_word]))
            
            # # dfs to find all the paths
            # res = []
            # if found:
            #     self.dfs(beginWord, endWord, graph, [], res)
            # return res
        path_list = []
        for i in wordList:
            def hamming_distance(i, endWord):
                if len(i) != len(endWord):
                    raise ValueError("Strings must be of the same length")
                return sum(ch1 != ch2 for ch1, ch2 in zip(i, endWord))
            print(hamming_distance(i, endWord))
            if hamming_distance(i, endWord) == 1:
                print(i)
                path_list.append(i)
                endWord = i

            
        
        
            