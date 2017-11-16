from django.test import TestCase
from .models import Creator, Project

# Create your tests here.
class CreatorTestClass(TestCase):
    '''
    Test case for Creator class
    '''

    # Set Up method
    def setUp(self):
        '''
        Method that sets up a Creator instance before each test
        '''
        # Create a creator instance
        self.new_creator = Creator(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    def test_instance(self):
        '''
        Test case to check if self.new_creator in an instance of Creator class
        '''
        self.assertTrue( isinstance(self.new_creator, Creator) )

    def test_save_creator(self):
        '''
        Test case to check is a creator is saved in the database
        '''
        self.new_creator.save_creator()
        creators = Creator.objects.all()
        self.assertTrue( len(creators) > 0 )

    def test_delete_creator(self):
        '''
        Test case to check if a creator is deleted from the database
        '''
        self.new_creator.save_creator()
        creators = Creator.objects.all()
        self.new_creator.delete_creator()
        self.assertTrue( len(creators) == 0)

    def test_get_creators(self):
        '''
        Test case to check if all creators are gotten from the database
        '''
        self.new_creator.save_creator()
        gotten_creators = Creator.get_creators()
        creators = Creator.objects.all()
        self.assertTrue( len(gotten_creators) == len(creators))


class ProjectTestClass(TestCase):
    '''
    Test case for Project class
    '''

    # Set Up method
    def setUp(self):
        '''
        Method that sets up a Project instance before each test
        '''
        # Create and save a creator instance
        self.james = Creator(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_creator()

        # Create a project instance
        self.new_project = Project(name = 'Python James', description ='Python James is Muriuki who wrote Python content for Moringa School', git_hub_link='https://github.com/tester/test-link', deployed_link='https://test/deployed-link', creator=self.james)

    def test_instance(self):
        '''
        Test case to check if self.new_project in an instance of Project class
        '''
        self.assertTrue( isinstance(self.new_project, Project) )

    def test_save_project(self):
        '''
        Test case to check is a Project is saved in the database
        '''
        self.james.save_creator()
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue( len(projects) > 0 )

    def test_delete_project(self):
        '''
        Test case to check if an project is deleted from the database
        '''
        self.new_project.save_project()
        projects = Project.objects.all()
        self.new_project.delete_project()
        self.assertTrue( len(projects) == 0 )

    def test_get_projects(self):
        '''
        Test case to check if all projects are gotten from the database
        '''
        self.new_project.save_project()
        gotten_projects = Project.get_projects()
        projects = Project.objects.all()
        self.assertTrue( len(gotten_projects) == len(projects))


