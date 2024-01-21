from nlplogic import corenlp

def test_get_phrase():
    assert 'golden state' in corenlp.get_phrases("Golden State Warriors")