from django.db import models


class Prediction(models.Model):
    text = models.TextField(null=True)
    class_ind = models.IntegerField(db_column='class')

    def __str__(self):
        return self.text + ': ' + str(self.class_ind)
