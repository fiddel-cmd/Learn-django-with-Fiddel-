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
