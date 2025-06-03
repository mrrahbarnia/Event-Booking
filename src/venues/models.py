from django.db import models

from common.models import BaseModel


class Venue(BaseModel):
    name = models.CharField(max_length=250, unique=True)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name


class Salon(BaseModel):
    name = models.CharField(max_length=250)
    description = models.TextField()
    total_seats = models.IntegerField()
    venue = models.ForeignKey(to=Venue, on_delete=models.CASCADE, related_name="salons")

    def __str__(self) -> str:
        return self.name


class Floor(BaseModel):
    name = models.CharField(max_length=250)
    floor_number = models.PositiveIntegerField()
    seat_map = models.JSONField()
    salon = models.ForeignKey(to=Salon, on_delete=models.CASCADE, related_name="floors")

    def __str__(self) -> str:
        return self.name
