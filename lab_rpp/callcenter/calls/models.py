from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.email})"

class Reason(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Operator(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.email})"

class Status(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class Call(models.Model):
    phone_number = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='calls')
    reason = models.ForeignKey(Reason, on_delete=models.SET_NULL, null=True, related_name='calls')
    operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True, related_name='calls')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    problem_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Call from {self.phone_number} at {self.date_time}"
