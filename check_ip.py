"""
A regex to check if an input is a correct ip or not
"""

import re

pattern = r"^(((25(0|1|2|3|4|5){1})|(1\d\d){1}|((1|2|3|4|5|6|7|8|9)\d){1}|(\d){1})\.){3}((25(0|1|2|3|4|5){1})|(1\d\d){1}|((1|2|3|4|5|6|7|8|9)\d){1}|(\d){1})\b"

def main():
    try:
        n = int(input("Enter the number of test(s):"))
    except Exception as e:
        print(e)

    try:
        for _ in range(n):
            ip = str(input("Enter ip to check:"))
            checkip = re.match(pattern, ip)
            if checkip:
                print("\"{}\" is a valid ip".format(ip))
            else:
                print("\"{}\"1 is NOT a valid ip".format(ip))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()