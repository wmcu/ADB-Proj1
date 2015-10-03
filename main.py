import sys
import urllib
from search_web import search_web
from collect_feedback import collect_feedback
from expand_query import expand_query


def main(account_key, precision, queries):
    print "Parameters:"
    print "Client key =", account_key
    print "Query =", queries
    print "Precision =", precision
    print ""

    while True:
        # Search web pages by given queries
        results, query_url = search_web(account_key, queries)
        print "URL:", query_url
        print "Total number of results:", len(results)

        if len(results) < 10:
            print "Too few docs found, done"
            break

        # Collect user feedback
        print "Bing Search Results:\n======================"
        feedbacks = collect_feedback(results)
        this_precision = 1.0 * sum(feedbacks) / len(feedbacks)
        print "======================"
        print "Feedback summary"
        print "Query:", queries
        print "Precision:", this_precision
        if this_precision == 0:
            print "No relevant doc found, abort"
            break
        if this_precision >= precision:
            print "Desired precision reached, done"
            break
        print "Still below the desired precision:", precision

        # Expand queries by relevance feedback
        queries = expand_query(queries, results, feedbacks)
        print "New Query:", queries


if __name__ == '__main__':
    account_key = sys.argv[1]
    precision = float(sys.argv[2])
    queries = sys.argv[3].split()
    main(account_key, precision, queries)
