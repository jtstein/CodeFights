"""
Jordan Stein
7/9/2017

You are given the string s. Your friend just asked you if it's possible to change the string from s to a string t by removing some characters from it. You're a pro at programming, so you decided to create a program to determine this.

Example

For s = "ceoydefthf5iyg5h5yts" and t = "codefights", the output should be
convertString(s, t) = true.
For s = "addbyca" and t = "abcd", the output should be
convertString(s, t) = false.
Input/Output

[time limit] 4000ms (py3)
[input] string s

A string with alphanumeric characters.

Guaranteed constraints:
1 ≤ s.length ≤ 1000.

[input] string t

A string with alphanumeric characters.

Guaranteed constraints:
1 ≤ t.length ≤ 1000.

[output] boolean

Return true if it is possible to convert s to t, otherwise return false.
"""

def convertString(s, t):
    tList = []
    tindex = 0
    for char in s:
        if char == t[tindex]:
            tList.append(char)
            tindex+=1
            if tindex >= len(t):
                return t == ''.join(tList)
    return t == ''.join(tList)