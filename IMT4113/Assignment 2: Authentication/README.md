# Quality Check for Changed Password
The following is the task description for the assignment.
## Assumptions
- Let your old password is x
- Length of x is 8 characters
## Rules
- Let y be your new password
- y ≠ x
## Policies in the New password
- Must contain at least one uppercase (A,B,C..), one lowercase (a,b,c …), one number(0-9)and one special character
- Not same as x (Mandatory)
- Length >=8
- Length >=8
- Not a Palindrome
- Not a Dictionary word
- Consective Alphabets should not be same
- Total 9 password Criteria (pc):
``
If y satisfies p rules
then
Password (y) is w=((p*100)/pc) weak!
``
- Total 9 password Criteria:
``
If w < 50%
Display: «password is too weak to store, Try again»!
``
- Total 9 password Criteria:
``
If w > 50%
Display: «Well Done! Good to Go»
``
## Input sources
- Use any dictionary of your choice with at least 100 words
- Or use: https://learnersdictionary.com/3000-words/alpha/a/2
- For special characters use following source: https://owasp.org/www-community/password-special-characters

## Test cases
- A!1apa1!A
- 1#aAa#1
- Apple12#
- Word121#&
- A!1ap22pa1!A
- Qwerty121#
- Welcome42!
- JamesBond007!
- OrangeBall0#

## Programming
Create the following functions/script in Matlab:
1.  function or script PasswordQualityCheck:
    * this script/function should take input <old password> and asks user for <new password>
    * User supplies <new password>
    * System should display both <old password> and <new password>
    * System displays all the <policies> which are satisfied by the <new password>
    * System should also display the strength of the <new password> based on the 9 suggested policies
    * Upon weak password, system should prompt the user back to enter <new password> again
2. Use the given test cases
