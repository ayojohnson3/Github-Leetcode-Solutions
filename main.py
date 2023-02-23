
def longestPalindrome(string):
    # Edge cases
    if string == None or len(string) < 1:
        return "None"
    
    start, end = 0, 0
    for i in range(len(string)):
        len1 = expandAroundCenter(string, i, i) #racecar - case1
        len2 = expandAroundCenter(string, i, i +1) #abba - case2
        length =  max(len1, len2)
        
        if length > end - start:
            start = i - (length-1)//2
            end = i + length // 2
    
    return string[start:end + 1]


def expandAroundCenter(string, left, right):
    L = left
    R = right

    while L >= 0 and R < len(string) and string[L] == string[R]:
        L -= 1
        R += 1
    
    return R - L - 1

print(longestPalindrome("can"))