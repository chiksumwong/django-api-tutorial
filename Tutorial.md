# Tutorial 2: Request and Responses
## Request, Response, Status
- Using DRF's "Request" replace Django's "request.POST"
- Using DRF's "Response" replace Django http's "HttpResponse" and "JsonResponse"
- Using DRF's "Status" object

## Wrapping API views
- "@api_view" for function based views
- "APIView" for class-base views

## Format Suffixes API for "Browsable API" (options)
- will return the api with different format which define by request header set "Accept", e.g. "application/json", "text/html"
- able to return a web-browsable API ("text/html" format)
1. set "format=None" in view's function
2. import "format_suffix_patterns" in app's urls

# Tutorial 3: Class-base Views
## Class-base Views
- allow us to easily compose reusable bits of behavior by using "Mixins"

## Mixins (Python Multi Inheritance)
- System will provide the basic CURD behavior
- But we can rewrite the behavior which we want by Mixinsing the code that we write and system default
- reduce the code which need to write

## Generics
- a set of already mixed-in generic views that DRF provides

# Tutorial 4: Authentication & Permissions
### Aims
- Code snippets are always associated with a creator.
- Only authenticated users may create snippets.
- Only the creator of a snippet may update or delete it.
- Unauthenticated requests should have full read-only access.

## Authentication
- Must using the Django's User Model if you want to use the Django's auth system

Create User
```python
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
user.save()
```

Change Password
```python
u = User.objects.get(username='john')
u.set_password('new password')
u.save()
```

User Authentication - Login
```python
from django.contrib.auth import authenticate, login
user = authenticate(username='john', password='secret')
if user is not None:
    login(request, user)
    # A backend authenticated the credentials
else:
    # No backend authenticated the credentials
```

User Authentication - Logout
```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
```

User Authentication
```python
if request.user.is_authenticated:
    # Do something for authenticated users.
else:
    # Do something for anonymous users.
```

## Object Level Permission


## Field Level Permission