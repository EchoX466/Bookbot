def get_book_text():
	with open("books/frankenstein.txt") as f:
		print(f.read())

def main():
	get_book_text()

if __name__ == "__main__":
	main()
