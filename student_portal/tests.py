from django.test import TestCase

from .models import Student


class StudentModelTests(TestCase):
	def test_student_string_representation_uses_name(self):
		student = Student(name="Amina", registration_number="ST-001", email="amina@example.com", course="Django")

		self.assertEqual(str(student), "Amina")


class HomeViewTests(TestCase):
	def test_home_lists_students_in_name_order(self):
		Student.objects.create(name="Zuri", registration_number="ST-002", email="zuri@example.com", course="Python")
		Student.objects.create(name="Amina", registration_number="ST-001", email="amina@example.com", course="Django")

		response = self.client.get("/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Amina")
		self.assertContains(response, "Zuri")
		self.assertLess(response.content.index(b"Amina"), response.content.index(b"Zuri"))


class StudentCreateViewTests(TestCase):
	def test_create_student_view_saves_a_new_student(self):
		response = self.client.post("/create/", {
			"name": "Lina",
			"registration_number": "ST-003",
			"email": "lina@example.com",
			"course": "Django",
		})

		self.assertEqual(response.status_code, 302)
		self.assertTrue(Student.objects.filter(name="Lina", email="lina@example.com").exists())
