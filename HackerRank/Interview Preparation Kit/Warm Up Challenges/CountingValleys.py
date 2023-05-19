# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

def countingValleys(steps, path):
    # count for the valleys when level is less than 0, same amount of U & D above level > 0 do not matter
    level = 0
    valley_count = 0
    tracking_dict = {'U': 0, 'D': 0}
    for c in path:
        if c == 'D':
            level -= 1
            tracking_dict['D'] += 1
        elif c == 'U':
            level += 1
            if(tracking_dict['D'] > 0 and level == 0):
                tracking_dict['D'] = 0
                valley_count += 1

    return valley_count
        

if __name__ == '__main__':
    steps = 8
    path = 'UDDDUDUU'
    # path = 'DDUUUUDD'
    print(countingValleys(steps, path))
