from get_data import *

methods = {
    'get': lambda url: requests.get(url),
    'post': lambda url, data: requests.post(url, data),
    'put': lambda url, data: requests.put(url, data)
}


def check_args(args):
    if not args.method:
        return -1
    if not args.endpoint:
        return -2
    if not args.params:
        return -3
    return 0


if __name__ == '__main__':
    args = get_parser()
    if not args.method:
        args.method = 'get'
    check = check_args(args)
    print(get_data(args, methods))


