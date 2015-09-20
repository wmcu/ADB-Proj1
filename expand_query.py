from collections import defaultdict

def expand_query(queries, results, feedbacks):
    """Expand query
    returns a list of new queries
    """

    positive_text = ''
    negative_text = ''
    for result, feedback in zip(results, feedbacks):
        text = result['Title'] + ' ' + result['Description']
        if feedback == 1:
            positive_text += ' ' + text
        else:
            negative_text += ' ' + text

    positive_text_list = positive_text.split()
    negative_text_list = negative_text.split()

    positive_dict = defaultdict(int)
    negative_dict = defaultdict(int)

    positive_sum = 0
    negative_sum = 0

    for word in positive_text_list:
        if not word:
            continue
        positive_dict[word] += 1
        positive_sum += 1

    for word in negative_text_list:
        if not word:
            continue
        negative_dict[word] += 1
        negative_sum += 1

    positive_frequency_dict = defaultdict(float)
    negative_frequency_dict = defaultdict(float)

    for word, count in positive_dict.iteritems():
        positive_frequency_dict[word] = 1.0 * count / positive_sum

    for word, count in negative_dict.iteritems():
        negative_frequency_dict[word] = 1.0 * count / negative_sum

    sort_list = []
    for word, frequency in positive_frequency_dict.iteritems():
        weight = frequency - negative_frequency_dict[word]
        sort_list.append((word, weight))

    for word, frequency in negative_frequency_dict.iteritems():
        if word not in positive_frequency_dict:
            weight = 0.0 - frequency
            sort_list.append((word, weight))

    sort_list.sort(key=lambda x: x[1], reverse=True)

    count = 0
    for word, _ in sort_list:
        if isinstance(word, unicode):
            word = word.encode('ascii', 'ignore')
        if not word:
            continue
        if word not in queries:
            queries.append(word)
            count += 1
            if count >= 2:
                break

    return queries
