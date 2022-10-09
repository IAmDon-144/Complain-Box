from django.db import models
from profiles.models import Student, Teacher

statusType = (

    ('Submitted', 'Submitted'),
    ('Checking', 'Checking'),
    ('Solved', 'Solved'),
    ('Closed', 'Closed'),

)


privacyChoice = (
    ('Public', 'Public'),
    ('Anonymous', 'Anonymous'),
)


complainTypeChoice = (
    ('Management', 'Management'),
    ('Class', 'Class'),
    ('Against Teacher', 'Against Teacher'),
)


class Complain(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    privacy = models.CharField(max_length=10, choices=privacyChoice)
    complain_type = models.CharField(max_length=15, choices=complainTypeChoice)
    liked = models.ManyToManyField(Student,default=None,related_name='likes',blank=True)
    same = models.ManyToManyField(Student,default=None,related_name='same',blank=True)
    suggestions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}-{self.author.user.username}"

            
    def CommentCount(self):
        return self.comment_set.all().count() + self.commentbyteacher_set.all().count()

    class Meta:
        ordering = ['-created_at']

    


class Comment(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    post = models.ForeignKey(Complain,on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
    class Meta:
        ordering = ['-created']



class CommentByTeacher(models.Model):
    user = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    post = models.ForeignKey(Complain,on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
    class Meta:
        ordering = ['-created']



class Status(models.Model):
    type = models.CharField(max_length=10, choices=statusType,default="Submitted")
    post = models.OneToOneField(Complain,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.id}-{self.type}"

