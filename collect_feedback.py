
def collect_feedback(results):
    """Collect user feedback on query results
    returns a list of 0, 1 integers; 0 - irrelevant, 1 - relevant
    """
    feedback = []
    for index, result in enumerate(results):
        print 'Result', index + 1
        print 'URL:', result['Url']
        print 'Title:', result['Title']
        print 'Description:', result['Description']
        user_input = raw_input('Relevant (Y/N): ')
        feedback.append(1 if user_input == 'Y' else 0)

    return feedback
