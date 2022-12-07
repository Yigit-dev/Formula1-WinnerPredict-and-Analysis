from django.db import models

class FormulaDetail(models.Model):
    pos = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=50, null=True)
    pts = models.IntegerField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True) 
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
	    return str(self.pos)

# class TODO(models.Model):

#     title = models.CharField(max_length=64, null = False)
#     description = models.TextField(null = True)
#     is_complete = models.BooleanField(default = False)
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete = models.CASCADE,
#         related_name = "todo",
#         null = True,
#         blank = True
#     )
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.user.first_name} - {self.title}'