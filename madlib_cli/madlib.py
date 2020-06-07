import re


def read_template(path):
    """ The function takes data from text file and return a stripped string.

    Args:
        path (txt): txt file
    """
    with open(path, 'r') as madlib_read:
        text = madlib_read.read()
        return text


text_stored = read_template('assets/madlib.txt')

def find_words(sample, text_file):
    """Based on sample the function finds words and store it to an arr.

    Args:
        sample ([regex]): [regex pattern]
        text_file ([txt]): [text file]
    """
    words = re.findall(sample, text_file)
    return words


def template(sample, text_file):
    """ The function takes in a template string and returns a string with language parts removed.

    Args:
        sample ([regex]): [pattern]
        text_file ([txt]): [text file]
    """
    plain_text = re.sub(sample, '{}', text_file)
    return plain_text


def print_words():
    """Print words to a user and store user inputs into an list.
    """
    user_inputs = []
    for el in find_words("\{[a-zA-Z0-9\' -]*\}", text_stored):
        word = input(f'Give me: {el}')
        user_inputs.append(word)
    return user_inputs


def merge():
    """
    This function takes a template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
    """
    if input("Welcome to The Mad Libs Game!\n Would you like to play a game? \n Please enter yes(y) or no(n))") == 'y' or 'yes':
        user_inputs = print_words()
        store_template = template("\{[a-zA-Z0-9\' -]*\}", text_stored)
        inserted_template = store_template.format(*user_inputs)

        print('This is your story:', inserted_template)
        return inserted_template

    
def write(name):
    """Write down a new file with user inputs
    """
    with open(name, 'w') as write_file:
        result = write_file.write(merge())


if __name__ == "__main__": 
    write_content(madlib_result.txt)

