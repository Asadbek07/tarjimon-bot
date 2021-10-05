def write_to_file(chat_id):
	f = open("chat_ids.txt", "a")
	f.write(f"{chat_id} ")
	f.close()

def read_from_file():
	f = open("chat_ids.txt", "r")
	chat_ids = f.read().split(" ")
	return chat_ids	

