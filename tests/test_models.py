import unittest
from app import app, db
from app.models import Task

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_task_model(self):
        task = Task(title='Test Task', description='Test Task Description')
        db.session.add(task)
        db.session.commit()
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'Test Task Description')

if __name__ == '__main__':
    unittest.main()