def can_vote(age):
    if age >= 16:
        return 'Can vote!'
    return "Can't vote"

def age_category(age):
    if age <= 11:
        return 'Child'
    elif age <= 20:
        return 'Teenager'
    elif age <= 30:
        return 'Young'
    elif age <= 59:
        return 'Adult'
    return 'Elderly'

def enlistment_age(age, gender):
    if age >= 18 and gender =='M':
        return 'Can enlist!'
    return "Can't enlist!"