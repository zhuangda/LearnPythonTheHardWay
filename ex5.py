import math

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lb.
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight,
	my_age + my_height + my_weight)
	
# try something by myself
print "When I was %d, I like playing %s." % (12, 'Basketball')

print "What is this? It's %r." % 'nothing'
print "What is this? It's %s." % 'nothing'

# the following is new format character
print 'We are the {} who say "{}!"'.format('knights', 'Ni')
print '{1} and {0}'.format('spam', 'eggs')
print 'This {food} is {adj}.'.format(
		food='spam', adj='absolutely horrible')

print 'The value of PI is approximately {0:.3f}.'.format(math.pi)

table = {'Sjoerd': 4127, 'Anthony': 2123, 'Jason': 2131}
for name, phone in table.items():
	print '{1:10d} ==> {0:10}'.format(name, phone)
	
for name, phone in table.items():
	print '{0:10} ==> {1:10d}'.format(name, phone)
	
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print 'Jack: {Jack}'.format(Jack=4098)
print 'Jack: {[Jack]}'.format(table)

# pass the table as keyword arguments with the '**' notation
print 'Jack: {Jack}'.format(**table)

