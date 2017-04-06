''' Assuming every person will live for about 90 years,
    this script will show pictorially how many weeks 
    are left till we die. 
    So we must start working on our dreams right away!! '''
import sys
import datetime
from calendar import monthrange


if __name__ == '__main__':
    day = int(sys.argv[3])
    month = int(sys.argv[2])
    year = int(sys.argv[1])
    born = datetime.date(year, month, day)
    now = datetime.datetime.now().date()
    delta = now - born
    days_lived = delta.days
    age = days_lived / 365
    age_weeks = days_lived / 7
    weeks_left = 90 * 52 - age_weeks
    percent_life = (days_lived * 100.0) / (90 * 365)

    print 'Born: {}'.format(born)
    print 'Today: {}'.format(now)
    print 'Age: {}'.format(age)
    print 'Number of weeks lived: {}'.format(age_weeks)
    print 'Number of weeks till 90: {}'.format(weeks_left)
    print 'Percentage of life done: {}'.format(percent_life)

    count = 0
    for i in range(39):
        line = ''
        for j in range(120):
            if count < age_weeks:
                line = line + '*'
            else:
                line = line + '#'
            count = count + 1
        print line
