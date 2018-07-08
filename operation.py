import re


def str_proc(text):
    text = text.replace(' ', '')
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
