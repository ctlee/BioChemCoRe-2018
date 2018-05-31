import random
def cat_string(target_string):
    for i in range(2):
        newCatLocation = int(random.random() * len(target_string))
        target_string = target_string[:newCatLocation] + 'cat' + target_string[newCatLocation:]
        newMeowLocation = int(random.random() * len(target_string))
        target_string = target_string[:newMeowLocation] + 'meow' + target_string[newMeowLocation:]
    return target_string
    
