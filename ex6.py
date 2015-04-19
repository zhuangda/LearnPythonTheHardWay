x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "left "
e = "right"

print w + e

# use new format
x = "There are {:d} types of people.".format(10)
y = "Those who know {} and those who {}.".format(binary, do_not)

print x
print y

print "I said: {!r}.".format(x)
print "I also said: '{!s}'.".format(y)