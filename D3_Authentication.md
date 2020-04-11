# Authentication
- Must using the Django's User Model if you want to use the Django's auth system

### Create User
```python
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
user.save()
```

### Change Password
```python
u = User.objects.get(username='john')
u.set_password('new password')
u.save()
```

### User Authentication - Login
```python
from django.contrib.auth import authenticate, login
user = authenticate(username='john', password='secret')
if user is not None:
    login(request, user)
    # A backend authenticated the credentials
else:
    # No backend authenticated the credentials
```

### User Authentication - Logout
```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
```

### User Authentication
```python
if request.user.is_authenticated:
    # Do something for authenticated users.
else:
    # Do something for anonymous users.
```