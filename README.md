## Mad Libs Game

**Author:** Roman Sydoruk **Version:** 1.0.0

# Description

The application takes user inputs, inserts it into the given text and prints it out to user.

# Architecture

* Python 3.8.3
* Poetry
* Pytest

# Usage 
**read_template(path)** - this function takes data from text file and return a stripped string.\
**find_words(pat, text_file)** - based on sample the function finds words and store it in an arr.\
**template(pat, text_file)** - the function takes in a template string and returns a string with language parts removed.\
**print_words()** - print words to a user and store user inputs into an list.\
**merge()** - this function takes a template and a list of user entered language parts, and returns a string with the language parts inserted into the template.\
**write(name)** - Write down a new file with user inputs.\

[Link](https://github.com/sydoruk89/madlib-cli)