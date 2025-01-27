'''
Given a String, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forward and backwards.
A permutation is a rearrangement of a letters. The palindrome does not need
to be limited to just dictionary words. 
'''

palin_perm = "Tact Coa" #Taco Cat
not_palin_perm = "This is not a palindrome permutation"

# Time complexity: O(n)
# Space complexity: O(n)
def is_palin_perm(input_str):

    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

if __name__ == "__main__":

    A = 'Tact Coa' #Taco Cat
    B = 'This is not a palindrome permutation'
    C = 'race car'

    print(is_palin_perm(A))
    print(is_palin_perm(B))
    print(is_palin_perm(C))