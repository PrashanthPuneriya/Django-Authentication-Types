# Django-Learning

## Django

### auth1-Default-User

This project uses Django's default user model. It demonstrates the implementation of:-

* Registration
* Login and Logout redirect
* Custom django forms

### auth2-Abstract-User

This project extends AbstractUser. It demonstrates the implementation of:-

* Logging in via email and password
* forms.py
  * UserCreationForm
  * UserChangeForm
* admin.py customization using above forms
* Registration View logic

## DjangoRestFramework - DRF

### DRF-TokenBasedAuth

This project is an extension to auth2-AbstractUser. It combines auth2-AbstractUser, DRF and DRF's token authentication.
It uses rest_framework.authtoken i.e. Token Authentication.

It demostrates custom implementation of:-

* Registration
* Token generation for a new user
* Login
* ChangePassword

Registration and Login View logic has been implemented vaguely. It needs further improvements.

### DRF-allauth-djrestauth

### DRF-simpleJWT-AbstractUser

This project is an extension to auth2-AbstractUser. It combines auth2-AbstractUser, DRF and simple-jwt authentication.
It uses djangorestframework-simplejwt.

It demonstrates:-

* djangorestframework-simplejwt
* Login via email instead of username using AbstractUser
* Registration View logic
* RestAPI endpoints
