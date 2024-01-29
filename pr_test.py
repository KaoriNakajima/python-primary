import datetime

def sumInteger(a, b, c):
    return a+b+c


def list_loop(user_list: list[str]) -> list:
    for i in user_list:
        if i == "test":
            del i
    return user_list


def condition_check(level):
    if level < 100:
        print('Under 100')
    elif level < 50:
        print('Under 50')


def convert_date(date_string):
    return datetime.datetime.strptime(date_string, "yyyy-MM-dd")



if __name__ == "__main__":
    result = sumInteger(1,54,6)

    user_list: list[str] = []
    user_list.append('User1')
    user_list.append('User2')
    user_list.append(3)
    user_list.append('test')
    list_loop(user_list)

    condition_check(result)

    today = convert_date('20240125')
