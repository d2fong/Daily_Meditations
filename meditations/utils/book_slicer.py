

# algorithm: List of Text -> List of Text
# traverse through the list of text snippets
# if the text snippet begins with a token of the form <d.> Where d is a number,
# then add it to the current snippet to be jsonified
# while each subsequent text snippet does not begin with the form <d.>, append it 
# to the current text snippet to be jsonified.
# once we find a text snippet with the form <d.>, the text snippet is done, add it to the list

# Once we have the list of text snippets of the form:

# [
# 	{content: "....."},
# 	...
# 	...
# 	...
# ]

# write it to the file

# check whether or not the string begins with a token of the 
# form <d.>
def string_begins_with_numeric(s):
	if len(s) < 2:
		return False

	return s[-1] == '.' and s[0:len(s)-1].isdigit()


# def parse_book_into_paragraphs(f):
# 	with open(f, 'r') as file:
# 		data = file.read()


# 	# print data.split('\n')[:10]
# 	content = []
# 	index = 0
# 	for index in range(len(data)):
# 		if snippet == '':
# 			continue

# 		tokens = snippet.split(' ')
# 		header = tokens[0]
# 		json_snippet = {}
# 		if '.' in header and header[0:len(header) - 2].isdigit():
# 			content = 


# parse_book_into_paragraphs('meditations.txt')