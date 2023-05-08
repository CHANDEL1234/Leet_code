class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letter_set = set(letters)
        letter_list = list(letter_set)
        letter_list.sort()
        if target  not in letter_list:
            letter_list.append(target)
            letter_list.sort()
        if target == max(letter_list):
            return letters[0]
        if target != max(letter_list):
            Index = letter_list.index(target) + 1
            return letter_list[Index]
        
            



       
