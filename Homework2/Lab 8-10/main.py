#Dashiell Wendt 2033998

palindromeCandidate = input()

palindromeCondition = palindromeCandidate.replace(' ', '') == palindromeCandidate[::-1].replace(' ', '')
print(f'{palindromeCandidate} is{" not" if not palindromeCondition else ""} a palindrome')