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


def check_data(data):
        if data:
            for item in data:
                if item > 10:
                    for i in range(item):
                        if i % 2 == 0:
                            print(f"Even: {i}")
                        else:
                            if i > 5:
                                print(f"Odd and greater than 5: {i}")
                            else:
                                print(f"Odd and less than or equal to 5: {i}")
                else:
                    print("Item is 10 or less")
        else:
            print("No data")

def create_keyword_args(params: dict) -> tuple[dict]:

    def get_start_date_filter_param(str_from, key_prefix):
        kwargs = {}
        if str_from:
            str_from = str_from + ' 00:00:00'
            key_from = key_prefix + '__gte'
            kwargs.update({key_from: datetime.strptime(str_from, '%Y-%m-%d %H:%M:%S').replace(tzinfo=ZoneInfo('Asia/Tokyo'))})
        return kwargs

    def get_end_date_filter_param(str_to, key_prefix):
        kwargs = {}
        if str_to:
            str_to = str_to + ' 23:59:59'
            key_to = key_prefix + '__lte'
            kwargs.update({key_to: datetime.strptime(str_to, '%Y-%m-%d %H:%M:%S').replace(tzinfo=ZoneInfo('Asia/Tokyo'))})
        return kwargs

    def get_start_number_filter_param(str_from, key_prefix):
        kwargs = {}
        if str_from is not None:
            key_from = key_prefix + '__gte'
            kwargs.update({key_from: int(str_from)})
        return kwargs

    def get_end_number_filter_param(str_to, key_prefix):
        kwargs = {}
        if str_to is not None:
            key_to = key_prefix + '__lte'
            kwargs.update({key_to: int(str_to)})
        return kwargs

    options = {
        'company_name': {'func': lambda s: {'company_name__icontains': s.strip()}},
        'company_name_en': {'func': lambda s: {'company_name_en__icontains': s.strip()}},
        'apply_status': {'func': lambda s: {'apply_status__in': [int(status) for status in s]}},
        'contract_status': {'func': lambda s: {'contract_status__in': [int(status) for status in s]}},
        'inflow_route_type': {'func': lambda s: {'inflow_route_type__in': [int(status) for status in s]}},
        'is_deletable': {'func': lambda s: {'is_deletable__in': [eval(status) for status in s]}},
        'file_usage_permission': {'func': lambda s: {'file_usage_permission__in': [int(permission) for permission in s]}},


        # date rnage
        'service_available_start_date_to': {'func': lambda s: get_end_date_filter_param(s, 'service_available_start_date')},
        'service_available_start_date_from': {'func': lambda s: get_start_date_filter_param(s, 'service_available_start_date')},
        'trial_end_datetime_to': {'func': lambda s: get_end_date_filter_param(s, 'trial_end_datetime')},
        'trial_end_datetime_from': {'func': lambda s: get_start_date_filter_param(s, 'trial_end_datetime')},
        'created_at_to': {'func': lambda s: get_end_date_filter_param(s, 'created_at')},
        'created_at_from': {'func': lambda s: get_start_date_filter_param(s, 'created_at')},
        'subscription_end_date_to': {'func': lambda s: get_end_date_filter_param(s, 'subscription_end_date')},
        'subscription_end_date_from': {'func': lambda s: get_start_date_filter_param(s, 'subscription_end_date')},

        # number range
        'check_available_point_from': {'func': lambda s: get_start_number_filter_param(s, 'check_available_point')},
        'check_available_point_to': {'func': lambda s: get_end_number_filter_param(s, 'check_available_point')},
        'download_available_point_from': {'func': lambda s: get_start_number_filter_param(s, 'download_available_point')},
        'download_available_point_to': {'func': lambda s: get_end_number_filter_param(s, 'download_available_point')},
        'available_upload_file_byte_from': {'func': lambda s: get_start_number_filter_param(s, 'available_upload_file_byte')},
        'available_upload_file_byte_to': {'func': lambda s: get_end_number_filter_param(s, 'available_upload_file_byte')},
        'used_upload_file_byte_from': {'func': lambda s: get_start_number_filter_param(s, 'used_upload_file_byte')},
        'used_upload_file_byte_to': {'func': lambda s: get_end_number_filter_param(s, 'used_upload_file_byte')},

        # contract range
        'company_contract_list': {'func': lambda s: {'productcompanycontract__product_name__in': [int(product_name) for product_name in s]}},
    }

    kwargs, exclude_kwargs = {}, {}
    for k, v in params.items():
        if v is None:
            continue
        filter_option = options.get(k)
        if not filter_option:
            continue
        v = filter_option['func'](v)
        kwargs.update(v)

    return kwargs, exclude_kwargs


def get_today():
    return datetime.datetime.now(tz_info='UTC')


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
