import random
#takes chosen dice and number of roles to generate random value within parameters
def role_dice(x, y):
    points = (random.randint(1, x) * y)
    return points