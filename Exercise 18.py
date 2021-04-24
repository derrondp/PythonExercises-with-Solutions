# Question 18
# Level 3

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
import re
passList = input().split(",")


def validate(passList):
    isValid = True
    valid = []
    for passes in passList:
        if len(passes) < 6 or len(passes) > 12:
            isValid = False
            break
        elif not re.search('[a-z]', passes):
            isValid = False
            break
        elif not re.search("[_@$]", passes):
            isValid = False
            break
        elif not re.search('[A-Z]+', passes):
            isValid = False
            break
        elif not re.search(r'\d+', passes):
            isValid = False
            break
        elif re.search(r'\s', passes):
            isValid = False
            break
        else:
            isValid = True
            break
    
    if isValid:
        valid.append(passes)
    else:
        pass  

    if len(valid) > 1:
        return ','.join(valid)
    elif len(valid) == 1:
        return valid[0]
    
    return "No valid password!"


print(validate(passList=passList))
