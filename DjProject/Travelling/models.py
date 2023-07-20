from django.db import models
class Authentication(models.Model):
    # eid = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    class meta:
        db_table = "authentication"

# from django.db import models

# # class Member(models.Model):
# #   username = models.CharField(max_length=255)
# #   password = models.CharField(max_length=255)
# #   class meta:
# #     db_table="member"


# class User(models.Model):
#   email = models.CharField(max_length=255)
#   psw = models.CharField(max_length=255)
#   pswr = models.CharField(max_length=255)
#   class meta:
#     db_table="user"