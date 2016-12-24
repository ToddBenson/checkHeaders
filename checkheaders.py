#!/usr/bin python
from urllib import urlopen
import urllib2
import sys


def main():

    if len(sys.argv) < 2:
        print
        print('Please provide a fully-qualified path!\n')
        print('Usage: python gethead.py path\n')
        print('Example: python gethead.py http://www.google.com\n\n')
        sys.exit()
    else:
        response = urllib2.urlopen(sys.argv[1])
        print
        print('HTTP Header Analysis for ' + sys.argv[1] + ':' + '\n\n')

    if len(sys.argv) == 3:
        if sys.argv[2] == "-h":
            print("Header:")
            print(urlopen(sys.argv[1]).info())

    print("Checking for security headers...\n")

    # Check for cache-control
    if response.info().getheader('cache-control'):
        if 'no-cache' and 'no-store' in response.info().getheader('cache-control'):
            print('Cache-Control\t\t\t\t\tOK\t\t Cache-control is enabled.')
        else:
            print('Cache-Control\t\t\t\t\tCheck\t\t Check cache-control.')
    else:
        print('Cache-Control\t\t\t\t\tCheck\t\t Cache-control is not enabled.')

    # Check pragma
    if response.info().getheader('pragma') == 'no-cache':
        print('Pragma\t\t\t\t\t\tOK\t\t pragma was set properly.')
    else:
        print ('Pragma\t\t\t\t\t\tCheck\t\t pragma was not set.')

    # Check for content-type
    if 'text/html' in response.info().getheader('content-type'):
        print ('Content-Type\t\t\t\t\tOK\t\t content-type was set to text/html.')
    else:
        print ('Content-Type\t\t\t\t\tCheck\t\t content-type was not set to text/html.')

    # Check for content-type charset
    if 'charset=' in response.info().getheader('content-type'):
        print('Charset\t\t\t\t\t\tOK\t\t content-type charset was set.')
    else:
        print('Charset\t\t\t\t\t\tCheck\t\t Charset was not set')

    # check access-control-allow-origin:
    if response.info().getheader('access-control-allow-origin'):
        print('Access-Control-Allow-Origin\t\t\tOK\t\tAccess Control Policies are enforced.')
    else:
        print('Access-Control-Allow-Origins\t\t\tCheck\t\t Access Control Policies are not enforced.')

    # Check for strict-transport-security
    if response.info().getheader('strict-transport-security'):
        print('Strict-Transport-Security\t\t\tOK\t\t HTTP over TLS/SSL is enforced.')
    else:
        print('Strict-Transport-Security\t\t\tCheck\t\t HTTP over TLS/SSL is not enforced.')

    # X-Content-Type-Options
    if response.info().getheader('x-content-type-options') == 'nosniff':
        print('X-Content-Type-Options\t\t\t\tOK\t\t x-content-type-options was set properly.')
    else:
        print('X-Content-Type-Options\t\t\t\tCheck\t\t x-content-type-options was not set.')
    # x-content-security
    if response.info().getheader('x-content-security-policy'):
        print('X-Content-Security-Policy\t\t\tOK\t\t Content Security Policy is enforced.')
    else:
        print('X-Content-Security-Policy\t\t\tCheck\t\t Content Security Policy is not enforced.')

    # check x-download-options:
    if response.info().getheader('x-download-options') == 'noopen':
        print('X-Download-Options\t\t\t\tOK\t\t File Download and Open Restriction Policies are enforced.')
    else:
        print('X-Download-Options\t\t\t\tCheck\t\t File Download and Open Restriction Policies are not enforced.')

    # check x-xss-protection:
    if response.info().getheader('x-xss-protection') == '1; mode=block':
        print('X-XSS-Protection\t\t\t\tOK\t\t Cross-Site Scripting Protection is enforced.')
    else:
        print('X-XSS-Protection\t\t\t\tCheck\t\t Cross-Site Scripting Protection was not enable or was not set properly.')

    # Check for x-frame-options
    if response.info().getheader('x-frame-options'):
        if response.info().getheader('x-frame-options').lower() == 'deny' or 'sameorigin':
            print('X-Frame-Options\t\t\t\t\tOK\t\t Cross-Frame Scripting Protection is enabled.')
    else:
        print('X-Frame-Options\t\t\t\t\tCheck\t\t Cross Frame Scripting was not enabled or was not set properly.')

    print('\nChecking for information disclosure...\n')

    # Check for server
    if response.info().getheader('server'):
        print('Server\t\t\t\t\t\tCheck\t\t server was set.')
    else:
        print('Server\t\t\t\t\t\tOK\t\t server was not set.')

    # Check for x-powered-by
    if response.info().getheader('x-powered-by'):
        print('X-Powered-By\t\t\t\t\tCheck\t\t x-powered-by was set.')
    else:
        print('X-Powered-By\t\t\t\t\tOK\t\t x-powered-by was not set.')


if __name__ == '__main__':
    main()
