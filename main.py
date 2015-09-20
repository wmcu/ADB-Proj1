import base64
import urllib2
import sys

def main(account_key, precision, query):
    print "account_key:", account_key
    print "precision:", precision
    print "query:", query

if __name__ == '__main__':
    account_key = sys.argv[1]
    precision = sys.argv[2]
    query = sys.argv[3]
    main(account_key, precision, query)
