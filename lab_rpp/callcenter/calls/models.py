from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name


class Reason(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Operator(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Status(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Call(models.Model):
    phone_number = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='calls')  # one-to-many
    reason = models.ForeignKey(Reason, on_delete=models.SET_NULL, null=True, related_name='calls')  # many-to-one
    operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True, related_name='calls')  # many-to-one
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)  # one-to-one
    date_time = models.DateTimeField(auto_now_add=True)
    problem_resolved = models.BooleanField(default=False)

    def str(self):
        return f"Call from {self.phone_number} at {self.date_time}"


