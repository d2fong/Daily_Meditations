import json

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

def get_text_snippets(data):
	return data.split('\n')

def remove_empty_strings(snippet):
	return snippet == ''

def process_snippets(data):

	snippets = list(filter(None, data))

	paragraph_list = []
	curr_paragraph = ''
	for snippet in snippets:
		header = snippet.split(' ')[0]
		if string_begins_with_numeric(header):
			if len(curr_paragraph) > 0:
				paragraph_list.append(curr_paragraph)
			curr_paragraph = snippet
		else:
			curr_paragraph += '\n'
			curr_paragraph += snippet

	paragraph_list.append(snippets[-1])
	return paragraph_list

def map_paragraphs_to_json(paragraphs):
	json_rep = []
	for paragraph in paragraphs:
		paragraph_json = {}
		paragraph_json['content'] = paragraph
		json_rep.append(paragraph_json)

	return json_rep

def parse_book_into_paragraphs(src, dst):
	with open(src, 'r') as file:
		data = str(file.read())

	text_snippets = get_text_snippets(data)
	paragraphs = process_snippets(text_snippets)
	processed_paragraphs = map_paragraphs_to_json(paragraphs)
	with open(dst, 'w') as destination:
		destination.write(json.dumps(processed_paragraphs, indent=4, sort_keys=True, ensure_ascii=False))

parse_book_into_paragraphs('meditations.txt', 'output.json')