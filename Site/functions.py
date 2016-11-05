from django.contrib.auth import authenticate,login


def authenticated(request,username,password):

	user = authenticate(username=username,password=password)

	if user is not None:

		if user.is_active:
			login(request,user)
			return True
		else:
			return False
	else:
		return False
