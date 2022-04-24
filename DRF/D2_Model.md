# Model

## Basic ORM
```python
Model.objects.all()                               # Return all model object

m = Model(field1="Text1", date=timezone.now())  # Create one mode object
m.save()                                          # Save mode object

m.field1                                          # Return field 1 data

m.field1 = "Text2"                                # Update the field 1
m.save()                                          # Save mode object

Model.objects.filter(id=1)                        # Select id = 1 record
Model.objects.get(pk=1)                           # Get one id = 1 record
Model.objects.filter(field1_startswith='Tex')     # Select starts with

from django.utils import timezone
current_year = timezone.now().year
Model.objects.get(date_year=current_year)         # Select all record which year is current year

m = Model.objects.filter(id=1)                    # Delete                  
m.delete()
```
Return QuerySet:
https://www.liujiangblog.com/course/django/129
Not Return QuerySet:
https://www.liujiangblog.com/course/django/131
SQL Where
https://www.liujiangblog.com/course/django/132

## One to One, "OneToOneField"
if your want to connect your own user table with django auth model
```python
from django.conf import settings
from django.db import models

class MySpecialUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='supervisor_of',
    )
```

## One to Many, "ForeignKey" (FK must define in "MANY" side)
```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):                  # For Print Model Object and Admin Page
        return self.question_text

    def was_published_recently(self):   # Define the select method, return True or False
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

```python
q = Question.objects.get(pk=1)
q.was_published_recently()       # return True
q.choice_set.all()               # not any choice set
q.choice_set.create(choice_text='Not much', votes=0)  # create 1
q.choice_set.create(choice_text='The sky', votes=0)   # create 2
c = q.choice_set.create(choice_text='Just hacking again', votes=0) # create 3
c.question   # return question object 

q.choice_set.all()    # return 3 choice set
q.choice_set.count()  # return 3

from django.utils import timezone
current_year = timezone.now().year
Choice.objects.filter(question__pub_date__year=current_year) # question > pub_date > year, return 3 choice set

c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()
```

## One to Many (Self)
### Situation
- Comment System, one comment allow many people keep comment

```python
class Comment(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE) # parent comment with many sub comment
```

## Many to Many, "ManyToManyField", "through", "either one side"
```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',       ## Define middleware (middle table)
        through_fields=('group', 'person'),
    )

class Membership(models.Model):  # middleware (middle table)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)
```

## Mate
- db_table (set table name)
- ordering
- unique_together (validation - define the fields which is unique)
- 