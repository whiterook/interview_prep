__author__ = 'Sergey'

import sys
import datetime


def week_days(date_birth_str):
    try:
        date_birth = datetime.datetime.strptime(date_birth_str, '%m/%d/%Y').date()
        year_now = datetime.datetime.today().year
        year_of_birth = date_birth.year
        month_of_birth = date_birth.month
        day_of_birth = date_birth.day
        years = range(year_of_birth, year_now)
        for item in years:
            dta = datetime.date(item, month_of_birth, day_of_birth)
            week_day = datetime.date.strftime(dta, '%A')
            print(dta.year, week_day)
    except Exception as ex:
        print('Wrong date', ex)
    return


def main(dta):
    week_days(dta)
    return

if __name__ == '__main__':
    main(sys.argv[1])

