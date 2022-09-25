Given a string s, count special substrings in it. A Substring of S is said to be special if either of the following properties is satisfied. 

It starts with a vowel and ends with a consonant.
It starts with a consonant and ends with a vowel.
Examples:  

Input : S = "aba"
Output : 2
Substrings of S are : a, ab, aba, b, ba, a 
Out of these only 'ab' and 'ba' satisfy the
condition for special Substring. So the 
answer is 2.

Input : S = "adceba"
Output : 9

TwoCig Questions
Consider a string, s = "abc". An alphabetically-ordered sequence of substrings of s would be {"a", "ab", "abc", "b", "bc", "c"}. If we reduce this sequence to only those substrings that start with a vowel and end with a consonant, we're left with {"ab", "abc"}. The alphabetically first element in this reduced list is "ab", and the alphabetically last element is "abc". As a reminder:
Vowels: a, e, i, o, and u.
Consonants: b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, and z.

Complete the findSubstrings function in your editor. It has 1 parameter: a string, s, consisting of lowercase English letters (a − z). The function must find the substrings of s that start with a vowel and end with a consonant, then print the alphabetically first and alphabetically last of these substrings.

Input Format
The locked stub code in your editor reads a single string, s, from stdin and passes it to your function.

Constraints
3 ≤ length of s ≤ 5 × 105

Output Format
Your function must print two lines of output denoting the alphabetically first and last substrings of s that start with a vowel and end with a consonant. Print the alphabetically first qualifying substring on the first line, and the alphabetically last qualifying substring on the second line.

Sample Input 1
aba

Sample Output 1
ab
ab

Explanation 1
"ab" is the only possible substring which starts with a vowel (a) and ends with a consonant (b). Because we only have 1 qualifying substring, "ab" is both the alphabetically first and last qualifying substring and we print it as our first and second lines of output.

Sample Input 2
aab

Sample Output 2
aab
ab

Explanation 2
There are 2 possible substrings which start with a vowel and end with a consonant: "aab" and "ab". When ordered alphabetically, "aab" comes before "ab". This means that we print "aab" (the alphabetically first qualifying substring) as our first line of output, and we print "ab" (the alphabetically last qualifying substring) as our second line of output.

Sample Input 3
rejhiuecumovsutyrulqaeuouiecodjlmjeaummaoqkexylwaaopnfvlbiiiidyckzfhe

Sample Output 3
aaop
utyrulqaeuouiecodjlmjeaummaoqkexylwaaopnfvlbiiiidyckzfh

Explanation 3
There are 4830 substrings of s, but only 676 of them start with a vowel and end with a consonant. When ordered alphabetically, the first substring is "aaop" and the last substring is "utyrulqaeuouiecodjlmjeaummaoqkexylwaaopnfvlbiiiidyckzfh".
