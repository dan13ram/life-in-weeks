#!/usr/bin/env python
''' Assuming every person will live till 90 years,
    this script will show pictorially how many weeks
    are left till we die.
    So we must start working on our dreams right away!! '''
import sys
import datetime

TOTAL_LIFE = 90

if __name__ == '__main__':
    born = datetime.date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    now = datetime.datetime.now().date()
    days_lived = (now - born).days
    age = days_lived / 365
    age_weeks = days_lived / 7
    weeks_left = TOTAL_LIFE * 52 - age_weeks
    percent_life = (days_lived * 100.0) / (TOTAL_LIFE * 365)

    print 'Born: {}'.format(born)
    print 'Today: {}'.format(now)
    print 'Age: {}'.format(age)
    print 'Number of weeks lived: {}'.format(age_weeks)
    print 'Number of weeks till {}: {}'.format(TOTAL_LIFE, weeks_left)
    print 'Percentage of life done: {}'.format(percent_life)

    count = 0
    for i in range(TOTAL_LIFE * 52 / 130):
        line = ''
        for j in range(130):
            if count < age_weeks:
                line = line + '*'
            else:
                line = line + '#'
            count = count + 1
        print line
