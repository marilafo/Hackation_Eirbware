import random

gage_array = [
        ["You have to do 1 push-up"],
        ["You have to do 2 push-up"],
        ["You have to do 3 push-up"],
        ["You have to do 4 push-up"],
        ["You have to do 5 push-up"]
        ]

def get_gage():
    random.seed()
    gage = random.randrange(0, len(gage_array))
    return [gage]
        


