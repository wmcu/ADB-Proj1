
def collect_feedback(results):
	"""Collect user feedback on query results
    returns a list of 0, 1 integers; 0 - irrelevant, 1 - relevant
    """
	feedback = []
	for result in results:
		print result
		user_input = raw_input('Relevant (Y/N): ')
		feedback.append(1 if user_input == 'Y' else 0)
