import re


def str_proc(text):
    text = text.replace(' ', '')
    if  re.search('[^\d]', text[0]):
        text = '0' + text
    # 匹配非数字非四则运算符号or有连续重复运算符
    if re.search('[^\d\+\-\*/.]', text) or '' in re.split('[\+\-\*/]', text):
        return None
    return text

def operation(text):
    if not text:
        return 'Please input a valid equation'
    result = 0.0
    if not re.search('[\+\-\*/]', text):
        return float(text)
    elif '+' in text:
        numbers = text.split('+')
        for number in numbers:
            result += operation(number)
    elif '-' in text:
        numbers = text.split('-')
        result += operation(numbers[0])
        for number in numbers[1:]:
            result -= operation(number)
    elif '*' in text:
        numbers = text.split('*')
        result += operation(numbers[0])
        for number in numbers[1:]:
            result *= operation(number)
    elif '/' in text:
        numbers = text.split('/')
        result += operation(numbers[0])
        for number in numbers[1:]:
            result /= operation(number)
    return result

if __name__ == '__main__':
    #print(operation("I AM  A man"))
    print(str_proc('/2'))
    print(''in  '0//3'.split('/'))
    print(re.split('[\+\-\*/]', '1++2--3'))
    #print(operation('0//3'))
    print(operation('2.5/2'))
    print(str_proc('2.1 + 4 /2 - 3 * 1.1'))
    print(operation(str_proc('2.1 + 4 /2 - 3 * 1.1')))
    print(str_proc('1 + 4/2 - 6/3'))
    print(operation(str_proc('1 + 4/2 - 6/3')))



