import requests
import argparse
import pprint
import sys


def isurl(url):
    return True if url.lower().startswith("http://") or url.lower().startswith("https://") else False


def get_response_headers(target_url):
    # return requests.request("GET", target_url, verify=False).headers
    return requests.request("GET", target_url).headers


def check_headers(target_url, headers_file):
    if not isurl(target_url):
        return "['" + target_url + "', 'Invalid URL']"

    results = [target_url]
    request_headers = get_response_headers(target_url)
    results.append(request_headers)
    for header in get_headers_to_check(headers_file):
            try:
                results.append(header + ": " + request_headers[header])
            except KeyError:
                results.append(header + ": header not found")
    return results


def get_headers_to_check(headers_file):
    if headers_file is not None:
        headers_list = read_file_to_list("./headers.txt")
    else:
        headers_list = read_file_to_list("./default-headers.txt")

    return headers_list


def read_file_to_list(filename):
    with open(filename, 'r') as f:
        new_list = f.read().splitlines()
    return new_list


def get_targets(targets_file):
    return read_file_to_list(targets_file)


def check_targets(targets_file, headers_file):
    results = []
    for target in get_targets(targets_file):
        results.append(check_headers(target.strip("\n"), headers_file))
    return results


def check_arguments(args):
    if args.file is None and args.url is None:
        print("You need to specify a URL or a file with host URLs")
        exit(0)
    if args.file and args.url:
        print("Specify either a URL or a file with URLs")
        exit(0)


# need test
def run(args):
    if args.file:
        return check_targets(args.file, args.response)
    else:
        return check_headers(args.url, args.response)


# need test
def print_results(args, results):
    print(results)
    if args.file:
        for header in range(1, len(results)):
            print(results[header][0])
            if args.printheader:
                pprint.pprint(results[header][1])
            for result in range(2, len(results[header])):
                print(results[header][result])
            print("\n\n")
    else:
        print(results[0])
        if args.printheader:
            pprint.pprint(results[1])
        for header in range(2, len(results)):
            print(results[header])
        print("\n\n")
    return True


def parse_args(args):
    parser = argparse.ArgumentParser('Check for HTTP Response security headers')
    parser.add_argument("-u", "--url", type=str, help="The target URL")
    parser.add_argument("-f", "--file", type=str, help="A file containing target URLs")
    parser.add_argument("-r", "--response", type=str, help="A file containing headers to check")
    parser.add_argument("-p", "--printheader", help="Print the HTTP Response header", action="store_true")

    return parser.parse_args(args)


def main():
    parser = parse_args(sys.argv[1:])
    check_arguments(parser)
    # need test
    print_results(parser, run(parser))


if __name__ == "__main__":
    main()
