import requests
import argparse


methods = {
    'get': lambda url: requests.get(url),
    'post': lambda url, data: requests.post(url, data)
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
    parser = argparse.ArgumentParser(description="Work with api")
    parser.add_argument('--method', type=str)
    parser.add_argument('--endpoint', type=str)
    parser.add_argument('--params', type=str)
    args = parser.parse_args()
    check = check_args(args)
    try:
        if args.endpoint:
            if args.method in methods:
                response = methods[args.method](args.endpoint)
                print(response.status_code)
    except requests.RequestException as e:
        print(e)


