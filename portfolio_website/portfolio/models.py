from django.db import models

# Create your models here.
class Creator(models.Model):
    '''
    Class that defines a Creator for a project
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_creator(self):
        '''
        Method to save a new Creator to the database
        '''
        self.save()

    def delete_creator(self):
        '''
        Method to delete a Creator from the database
        '''
        self.delete()

    @classmethod
    def get_creators(cls):
        '''
        Method that gets all creators from the database

        Returns:
            creators : list of creator objects from the database
        '''
        creators = Creator.objects.all()
        return creators

class Project(models.Model):
    '''
    Class that defines a Project
    '''
    name = models.CharField(max_length=60)
    description = models.TextField()
    git_hub_link = models.CharField(max_length=255)
    deployed_link = models.CharField(max_length=255)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_project(self):
        '''
        Method to save a new Project to the database
        '''
        self.save()

    def delete_project(self):
        '''
        Method to delete a Project from the database
        '''
        self.delete()

    @classmethod
    def get_projects(cls):
        '''
        Method that gets all projects from the database

        Returns:
            projects : list of project objects from the database
        '''
        projects = Project.objects.all()
        return projects


