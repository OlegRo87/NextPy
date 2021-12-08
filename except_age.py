class UnderAge(Exception):

    def __init__(self, age):
        self._age = age

    def __str__(self):
        return "Provided argument %s is not a legal integer." % self._age

    def get_age(self):
        return self._age


def send_invitation(name, age):
    if int(age) < 18:
        raise UnderAge(age)
    else:
        print("You should send an invite to " + name)



def main():
    result = send_invitation("oleg", 20)

main()
