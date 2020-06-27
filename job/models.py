from django.db import models

# Create your models here.

'''
#Important notes:
    * django modles field:
        - HTML widget
        - validation
        - DB size


'''
jobTypeChoices = (
                  ('FT', 'Full-time'),
                  ('PT', 'Part-time'),
                  ('F', 'Freelancer')
                 )

class Job(models.Model):        ## this class in database = the table
    title = models.CharField(max_length=100)        ## this variable in database = the column
    # locatin =
    jobType = models.CharField(max_length=15, choices=jobTypeChoices)
    description = models.TextField(max_length= 1000)
    publishedAt = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    

