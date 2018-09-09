import random
import string

#Place all the utility functions here
def codeGenerator(size=6,chars=string.ascii_lowercase+string.digits):
	new_code=""
	for i in range(size):
		new_code+=random.choice(chars)
	return new_code



def createShortCode(instance,size=6):
	new_code=codeGenerator(size=size)
	klass=instance.__class__
	code_exists=klass.objects.filter(shortcode=new_code).exists()
	if code_exists:
		return createShortCode(size=size)
	return new_code