"""How to check if a pattern is valid regex or not."""
import re


def check_regex():
    """Using re.complie to check if an input string a valid regex or not.
    
    Input:
    n: number of string you want to test
    the next n lines are your inputs. Each input wil return True if your input
    is a valid regex pattern, or False if it's not.
    """
    for _ in range(int(input())):
        try:
            re.compile(input())
        except Exception:
            print('False')
        else:
            print('True')


if __name__ == '__main__':
    check_regex()

