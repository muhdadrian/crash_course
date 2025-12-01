favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

name = input('Please enter your name: ')

if name not in favorite_languages.keys():
	print(f"{name.title()}, please take our poll!")

			