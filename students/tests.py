from django.test import TestCase

from student_portal.models import Student


class StudentListViewTests(TestCase):
    def test_students_route_lists_students(self):
        Student.objects.create(
            name='Amina',
            registration_number='ST-001',
            email='amina@example.com',
            course='Django',
        )

        response = self.client.get('/students/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Amina')


class StudentCreateViewTests(TestCase):
    def test_create_page_accepts_student_data(self):
        response = self.client.post(
            '/students/create/',
            {
                'name': 'Brian',
                'registration_number': 'ST-002',
                'email': 'brian@example.com',
                'course': 'Python',
            },
        )

        self.assertRedirects(response, '/students/')
        self.assertTrue(Student.objects.filter(registration_number='ST-002').exists())

    def test_create_page_shows_validation_errors(self):
        response = self.client.post('/students/create/', {'name': 'Incomplete'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        self.assertEqual(Student.objects.count(), 0)
