import argparse
import requests

def get_parser():
    parser = argparse.ArgumentParser(description="Work with api")
    parser.add_argument('--method', type=str)
    parser.add_argument('--endpoint', type=str)
    parser.add_argument('--params', type=list, nargs='+')

    return parser.parse_args()


def make_param(params):
    dct = dict()
    for p in params:
        dct[p[0]] = p[2]
    return dct

def get_data(args, methods='get'):
    try:
        if args.endpoint:
            if args.method in methods:
                if args.params:
                    data = make_param(args.params)
                    response = methods[args.method](args.endpoint, data)
                else:
                    response = methods[args.method](args.endpoint)
                return response.headers
    except requests.RequestException as e:
        print(e)