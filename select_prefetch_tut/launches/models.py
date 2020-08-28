from django.db import models
from django_hint import StandardModelType


class Launch(models.Model, StandardModelType):
    date = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=100)
    rocket = models.ForeignKey(
        "launches.Rocket",
        null=True,
        blank=True,
        related_name="launches",
        on_delete=models.SET_NULL,
    )
    crew = models.ManyToManyField("launches.Crew", blank=True, related_name="launches")
    launch_pad = models.ForeignKey(
        "launches.LaunchPad",
        null=True,
        blank=True,
        related_name="launches",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.__class__.__name__}({self.pk}): {self.name}"


class Rocket(models.Model, StandardModelType):
    name = models.CharField(max_length=100)
    core = models.ForeignKey(
        "launches.Core",
        null=True,
        blank=True,
        related_name="rocket",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.__class__.__name__}({self.pk}): {self.name}"


class Core(models.Model, StandardModelType):
    serial = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.__class__.__name__}({self.pk}): {self.serial}"


class Crew(models.Model, StandardModelType):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.__class__.__name__}({self.pk}): {self.name}"


class LaunchPad(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.__class__.__name__}({self.pk}): {self.name}"
