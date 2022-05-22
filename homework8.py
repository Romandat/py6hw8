from datetime import datetime, timedelta


users = [{'name': 'Bill, Jill', 'birthday': '2022-05-22'}, 
        {'name': 'Kim, Jan', 'birthday': '2022-05-24'},
        {'name': 'Rob, Bob', 'birthday': '2022-05-25'},
        {'name': 'Joe, Doe', 'birthday': '2022-05-26'}]

def get_birthdays_per_week(users_l: list) -> list:
    bd_list = []
    # today = datetime.now().date()
    today = datetime(year=2022, month=5, day= 20).date()
    week_interval = today + timedelta(weeks=1)
    days_to_shift = (0 - today.weekday() + 7) % 7
    first_monday = today + timedelta(days=days_to_shift)
    first_monday_day = first_monday.strftime('%A') 
    for u in users_l:
        for dict in users:
            if dict['name'] == u:
                bd_date = datetime.strptime(dict.get('birthday'), '%Y-%m-%d').date()
                bd_date_day = bd_date.strftime('%A')
                if week_interval > bd_date:
                    if 5 == bd_date.weekday() or bd_date.weekday() == 6:
                        bd_list.append(f'{first_monday_day}: {dict["name"]}')
                    else:
                        bd_list.append(f'{bd_date_day}: {dict["name"]}')
    # sort items in the result list
    days_index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    bd_list.sort(key=lambda x: days_index.index(x.split(':')[0]))
    for el in bd_list:
        el = el.split(':')
        print('{:>10}: {}'.format(el[0], el[1].strip()))

    return bd_list


# print(get_str_date("2021-05-24 17:08:34.149Z"))
print(get_birthdays_per_week(['Bill, Jill', 'Kim, Jan', 'Joe, Doe', 'Rob, Bob']))