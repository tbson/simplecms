from django.db import models


class VariableManager(models.Manager):
    def _seeding(self, index: int, single: bool = False, save: bool = True) -> models.QuerySet:
        from apps.variable.serializers import VariableBaseSr
        if index == 0:
            raise Exception('Indext must be start with 1.')

        def getData(i: int) -> dict:
            data = {
                'uid': "uid{}".format(i),
                'value': "value{}".format(i)
            }
            if save is False:
                return data

            instance = VariableBaseSr(data=data)
            instance.is_valid(raise_exception=True)
            instance = instance.save()
            return instance

        def getListData(index):
            return [getData(i) for i in range(1, index + 1)]

        return getData(index) if single is True else getListData(index)


# Create your models here.
class Variable(models.Model):
    uid = models.CharField(max_length=60, unique=True)
    value = models.CharField(max_length=250)

    objects = VariableManager()

    def __str__(self):
        return '{} - {}'.format(self.uid, self.value)

    class Meta:
        db_table = "variables"
        ordering = ['-id']
