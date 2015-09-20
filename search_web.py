__author__ = 'youhanwang'

import urllib2
import base64
import json


def search_web(account_key, query_list):
    bing_url_prefix = 'https://api.datamarket.azure.com/Bing/Search/Web?Query='
    pre_handled_query = '+'.join(query_list)

    handled_query = '%27' + pre_handled_query + '%27'
    top = '$top=10'
    encode_format = '$format=json'
    final_url = bing_url_prefix + handled_query + '&' + top + '&' + encode_format

    account_key_enc = base64.b64encode(account_key + ':' + account_key)
    headers = {'Authorization': 'Basic ' + account_key_enc}
    request = urllib2.Request(final_url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    json_content = json.loads(content)
    final_list = json_content['d']['results']

    return final_list

    # count = 1
    # for searchResult in final_list:
    #     print 'Result' + str(count)
    #     print 'URL: ' + searchResult['Url']
    #     print 'Title: ' + searchResult['Title']
    #     print 'Description ' + searchResult['Description']
    #     print '\n'
    #     count += 1
