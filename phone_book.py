# python3
 
 
def read_queries():
    n = int(input())
    return [input().split() for i in range(n)]
 
def write_responses(dicts, arr):
    """ process one array line."""    
    if len(arr) <= 1:
        return None
    result = None
    if len(arr) == 2:
        result = find_delete(dicts, arr[0], arr[1])
        if result is not None:
            print(result)
    if len(arr) > 2:
        add(dicts, arr[1], arr[2])
 
 
def find_delete(dicts, order, number):
    """ find or delete line phone number."""
    if order == "find":
        if dicts.get(number) is None:
            return "not found"
        if len(dicts[number]) < 1:
            return "not found"
        else:
            return dicts[number]
    if order == "del":
        if dicts.get(number) is not None:
            dicts[number] = ""
            return None
    return None
 
 
def add(dicts, number, name):
    """ add or overwrite a line in a phone book"""
    dicts[number] = name
    return None
 
 
def process_queries(queries):
	# print(queries)
	# Keep list of all existing (i.e. not deleted yet) contacts.
	contacts = dict()
	for line in queries:
		write_responses(contacts, line)
 
if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
