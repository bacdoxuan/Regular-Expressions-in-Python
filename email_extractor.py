import re

check_text = 'Enter your email list here to check: 123@gmail.com, .@..., some.one@erricsson.com, a#^*()@2d.c0m, dear^you@github.com'


def email_extractor(text):
    pattern = '(\w)+([\.-](\w+))*@(\w)+([\.-]\w)*(\.(\w+))'
    email_list = []
    find_iter = re.finditer(pattern, text)
    try:
        while True:
            n = next(find_iter)
            email_list.append(n.group())
    except Exception:
        pass
    return email_list


def main():
    inputtext = check_text
    result = email_extractor(inputtext)
    print(result)


if __name__ == '__main__':
    main()
