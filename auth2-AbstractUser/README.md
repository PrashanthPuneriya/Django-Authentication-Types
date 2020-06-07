# Django's-Abstract-User-Model

## Extension of auth1-DefaultUser

- settings.py
  - Changed `AUTH_USER_MODEL`
    - Used our Abstract User i.e. MyUser
- models.py
  - Abstract User to login using email but not username
- forms.py
  - UserCreationForm
  - UserChangeForm
- admin.py
  - Customized to use the above forms
- views.py
  - Registration Logic
- Logging in using email and password
