def scorePerson(openness,conscientiousness,extroversion,agreeableness,neuroticism,values,passions,similarities,importance,darkside):
    """
    returns personality score of given person
    """
    if openness > 8:
        openness = 8
    elif 5 < openness < 8:
        openness = 10
    elif 3 < openness < 5:
        openness = 5
    elif 1 < openness < 3:
        openness = 0
    elif 0 < openness < 1:
        openness = -3
    
    if 9 < conscientiousness < 10:
        conscientiousness = 8
    elif 6 < conscientiousness < 8:
        conscientiousness = 10
    elif 4 < conscientiousness < 6:
        conscientiousness = 5
    elif 2 < conscientiousness < 4:
        conscientiousness = 0
    elif 0 < conscientiousness < 2:
        conscientiousness = -5

    if extroversion > 9:
        extroversion = 8
    elif 7 < extroversion < 9:
        extroversion = 10
    elif 4 < extroversion < 6:
        extroversion = 8
    elif 2 < extroversion < 4:
        extroversion = 5
    elif 0 < extroversion < 2:
        extroversion = 0

    if agreeableness > 8:
        agreeableness = 5
    elif 6 < agreeableness < 8:
        agreeableness = 10
    elif 3 < agreeableness < 6:
        agreeableness = 7
    elif 2 < agreeableness < 3:
        agreeableness = 5
    elif 0 < agreeableness < 2:
        agreeableness = 4

    if neuroticism > 9:
        neuroticism = -5
    elif 7 < neuroticism < 9:
        neuroticism = -3
    elif 5 < neuroticism < 7:
        neuroticism = 0
    elif 3 < neuroticism < 5:
        neuroticism = 5
    elif 1 < neuroticism < 3:
        neuroticism = 10
    elif 0 < neuroticism < 1:
        neuroticism = 5

    val = len(values)
    pas = len(passions)
    sim = len(similarities)
    imp = len(importance)
    dar = len(darkside)
    n = val + pas + sim + imp + dar

    return openness + conscientiousness + extroversion + agreeableness + neuroticism + traitScore(val,n) + traitScore(pas,n) + traitScore(sim,n) + traitScore(imp,n) - traitScore(dar,n)


def traitScore(trait,total):
    ratio = trait/total
    if ratio > .2:
        return 10
    elif .1 < ratio < .2:
        return 9
    elif .05 < ratio < .1:
        return 8
    elif .03 < ratio < .05:
        return 5
    elif .01 < ratio < .03:
        return 3
    elif 0 < ratio < .01:
        return 0