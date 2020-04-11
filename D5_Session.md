# Session

## Cookie
- Save data in "Client Side"
- Save not importance data (e.g. token)

## Django's Session
### Session Store Type
- save in database (Use this way if not any special requirement)
- save in cache
- save in file
- save in cookie

## Usage
### Get
```python
s = request.session['session_name']
# OR
request.session.get(key, default=None)
```
### Set
```python
request.session['session_name'] = 'session_data'
```
### Delete
```python
del request.session['session_name']
```
### Delete All
```python
request.session.flush()
```
### Set Expiry
```python
request.session.set_expiry(300) #300s
request.session.set_expiry(datetime/timedelta) #after specify data
request.session.set_expiry(0) #after close browser
```
### Get Expiry Age
```python
request.session.get_expiry_age() # return seconds
```
### Get Expiry At Browser Close
```python
request.session.get_expire_at_browser_close() # return True/False
```
### Clean Expired Data
```python
request.session.clear_expired()
```

# Code Example
```python
ef login(request):
    if request.session.get('is_login', None):  # Not Repeated Login Allow
        return redirect('/login/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = 'Please check the content！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = 'User does not exist！'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = 'The password is incorrect！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())
```

```python
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    # Or use the following method
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")
```