from madlib_cli import __version__
from madlib_cli.madlib import read_template, find_words, template


def test_version():
    assert __version__ == '0.1.0'


def test_read_template():
    actual = isinstance(read_template('assets/madlib.txt'), str)
    expected = True
    assert actual == expected


def test_list():
    actual = find_words("\{(.*?)\}", read_template('assets/madlib.txt'))
    expected = ['Adjective', 'Adjective', 'A First Name', 'Past Tense Verb', 'A First Name', 'Adjective', 'Adjective', 'Plural Noun', 'Large Animal', 'Small Animal', "A Girl's Name", 'Adjective', 'Plural Noun', 'Adjective', 'Plural Noun', 'Number 1-50', "First Name's", 'Number', 'Plural Noun', 'Number', 'Plural Noun']
    assert actual == expected


def test_template():
    actual = template("\{.*?\}", '{1} apple, {2} mangos, {3} oranges')
    expected = '{} apple, {} mangos, {} oranges'
    assert actual == expected

