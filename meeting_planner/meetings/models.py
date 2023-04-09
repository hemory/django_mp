from django.db import models

from datetime import time

class Room(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()
    room_number = models.IntegerField()


    def __str__(self):
        return f"{self.name} on floor {self.floor} in room {self.room_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.date} at {self.start_time} for {self.duration} hour(s)"

