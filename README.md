## Django Custom User Model

This project provides a customizable Django user model, allowing you to create users and superusers with specific fields and permissions tailored to your application's requirements.

## Example Usages

### Create User

```python
from django.contrib.auth.models import User
from your_app.models import CustomUser

user = NewUser.objects.create_user(
    email='your_email@example.com',
    username='your_username',
    first_name='your_first',
    password='your_password'
)
```

### Create superuser

```python
from django.contrib.auth.models import User
from your_app.models import CustomUser

superuser = NewUser.objects.create_superuser(
    email='your_superuser_email@example.com',
    username='your_superuser_username',
    first_name='your_first',
    password='your_superuser_password'
)
```
