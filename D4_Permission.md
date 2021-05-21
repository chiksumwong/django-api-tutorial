# Permission
> https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

```python
from rest_framework import permissions
permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Add in view class
```

## Object Level Permission
- e.g. Only the creater anc update and delete the record

1. Create permissoins.py file

## Field Level Permission