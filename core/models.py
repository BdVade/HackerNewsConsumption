from django.db import models


# Create your models here.

class Base(models.Model):
    type_options = (
        ('job', 'job'),
        ('story', 'story'),
        ('comment', 'comment',),
        ('poll', 'poll'),
        ('pollopt', 'pollopt')
    )

    hacker_id = models.IntegerField(unique=True, null=True)
    time = models.TimeField(null=True)
    synced = models.DateTimeField(auto_now_add=True, null=True)
    type = models.CharField(choices=type_options, max_length=10)
    hn_deleted = models.BooleanField(default=False, null=True)
    author = models.CharField(max_length=200, null=True)
    text = models.CharField(max_length=5000, null=True)
    # kids = models.Re
    url = models.URLField(null=True)
    title = models.CharField(null=True, max_length=100)
    parent = models.ForeignKey('self', related_name='kids', on_delete=models.CASCADE, null=True)
    local = models.BooleanField(default=False)

    class Meta:
        ordering = ('-synced',)

