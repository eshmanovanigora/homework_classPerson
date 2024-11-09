from Person import Person

def test_User():
    person = Person('Nigora', '21')
    assert person.name == 'Nigora', 'should be Nigora'
    assert person.age == '21', 'not 21'

test_User()
