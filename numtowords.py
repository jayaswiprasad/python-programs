def number_to_words(num):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    if num == 0:
        return ones[0]
    elif num < 0:
        return 'minus ' + number_to_words(abs(num))

    words = ''
    if num // 1000000 > 0:
        words += number_to_words(num // 1000000) + ' million '
        num %= 1000000

    if num // 1000 > 0:
        words += number_to_words(num // 1000) + ' thousand '
        num %= 1000

    if num // 100 > 0:
        words += number_to_words(num // 100) + ' hundred '
        num %= 100

    if num > 0:
        if len(words) > 0:
            words += 'and '

        if num < 10:
            words += ones[num]
        elif num < 20:
            words += teens[num - 11]
        else:
            words += tens[num // 10 - 1]
            if num % 10 > 0:
                words += '-' + ones[num % 10]

    return words.strip()

num = 123456789
words = number_to_words(num)
print(words)
