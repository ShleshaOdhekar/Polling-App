from django.db import models

# Create your models here.
class Question(models.Model):
    ques_text= models.CharField(max_length=200)
    pub_date=models.DateTimeField('Date published')

    #display the ques_text
    def __str__(self):
        return self.ques_text

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE) #cascade-delete the choices along with the ques that is deleted 
    choice_text=models.CharField(max_length=200)
    votes= models.IntegerField(default=0)

    #display the choice_text
    def __str__(self):
        return self.choice_text
 
