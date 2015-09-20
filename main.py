import sys
import urllib.quote_plus
from search_web import search_web
from collect_feedback import collect_feedback
from expand_query import expand_query

def main(account_key, precision, queries):
    print "account_key:", account_key
    print "precision:", precision
    print "query:", queries
    results = search_web(account_key, queries)
    feedbacks = collect_feedback(results)
    this_precision = 1.0 * sum(feedbacks) / len(feedbacks)
    new_queries = expand_query(queries, results, feedbacks)

if __name__ == '__main__':
    account_key = sys.argv[1]
    precision = sys.argv[2]
    queries = sys.argv[3].split()
    main(account_key, precision, queries)
