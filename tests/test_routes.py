import unittest
from app import app, db
from app.models import Task

class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

        # Create a test task
        self.test_task = Task(title='Test Task', description='This is a test task')
        db.session.add(self.test_task)
        db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_task_route(self):
        response = self.app.post('/add', data=dict(
            title='Test Task',
            description='This is a test task'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_edit_task_route(self):
        response = self.app.post('/edit', data=dict(
            id=self.test_task.id,
            title='Updated Task',
            description='This is an updated test task'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()