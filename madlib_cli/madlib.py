import re, logging

try:
    def read_template(path):
        """ The function takes data from text file and return a stripped string.

        Args:
            path (txt): txt file
        """
        with open(path, 'r') as madlib_read:
            text = madlib_read.read()
            return text
except FileNotFoundError as error:
    print(error)


text_stored = read_template('assets/madlib.txt')


try:
    def find_words(pat, text_file):
        """Based on sample the function finds words and store it in an arr.

        Args:
            pat ([regex]): [regex pattern]
            text_file ([txt]): [text file]
        """
        words = re.findall(pat, text_file)
        return words
except Exception as ex:
    logging.exception(ex)


try:
    def template(pat, text_file):
        """ The function takes in a template string and returns a string with language parts removed.

        Args:
            pat ([regex]): [pattern]
            text_file ([txt]): [text file]
        """
        plain_text = re.sub(pat, '{}', text_file)
        return plain_text
except Exception as ex:
    logging.exception(ex)

try:
    def print_words():
        """Print words to a user and store user inputs into an list.
        """
        user_inputs = []
        for el in find_words("\{(.*?)\}", text_stored):
            word = input(f'Give me: {el} ')
            user_inputs.append(word)
        return user_inputs
except Exception as ex:
    logging.exception(ex)


try:
    if text_stored:
        def merge():
            """
            This function takes a template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
            """
            message = input('Welcome to The Mad Libs Game!\n Would you like to play a game? \n Please enter yes(y) or no(n)) ')
            if message.lower() == 'y' or message.lower() == 'yes':
                user_inputs = print_words()
                store_template = template("\{.*?\}", text_stored)
                inserted_template = store_template.format(*user_inputs)

                print('This is your story:', inserted_template)
                return inserted_template
            else:
                print('Thanks, see you next time!')
except Exception as ex:
    logging.exception(ex)


try:
    if merge():
        def write(name):
            """Write down a new file with user inputs.
            """
            with open(name, 'w') as write_file:
                result = write_file.write(merge())
                return result
except Exception as ex:
    logging.exception(ex)


if __name__ == "__main__":
    write('assets/madlib_result.txt')

