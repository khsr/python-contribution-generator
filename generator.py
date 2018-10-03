import sys, os
from subprocess import call
from datetime import date, timedelta
from random import randint

username = sys.argv[1]
password = sys.argv[2]
repository = sys.argv[3]

call('git init', shell=True)
call(
    'git remote add origin https://' + username + ':' + password + '@github.com/' + username + '/' + repository + '.git',
    shell=True)

time = '12:00:00'
offset = '-0500'
minimum = 0
maximum = 5
filename = 'README.md'
message = 'add one feature'

half = ' ' + time + ' ' + offset
current = date.today() - timedelta(days=365)
weekArr = []
sameCount = 0
for i in range(0, 365):
    if len(weekArr) == 6:
        weekArr = []
        sameCount = 0

    randCount = randint(0, 5)
    weekArr.append(randCount)
    sameCount = weekArr.count(randCount)

    if sameCount < 2:
        for k in range(0, randint(minimum, maximum)):
            complete = str(current) + half + ':' + str(k + 1)
            readme = open(filename, 'w+')
            readme.write(complete)
            # message = complete
            call('git add ' + filename, shell=True)
            call('git commit --date="' + complete + '" -m "' + message + '"', stdout=open(os.devnull, 'w'), shell=True)
            print 'Committing: ' + complete
    else:
        sameCount = 0

    call('git push origin master', shell=True)
    current = current + timedelta(days=1)
readme.close()
