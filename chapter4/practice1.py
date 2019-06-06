def practice(someParameter):
    concact = ', '.join(someParameter)
    answer = concact[:concact.rfind(',') + 1] + ' and' + concact[concact.rfind(',') + 1:]
    return answer

spam = ['apples', 'bananas', 'tofu', 'cats', 'sojabohnen', 'grundbirnen']
print(practice(spam))
