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


class StudentUpdateViewTests(TestCase):
	def test_edit_student_view_updates_existing_student(self):
		student = Student.objects.create(
			name="Lina",
			registration_number="ST-003",
			email="lina@example.com",
			course="Django",
		)

		response = self.client.post(f"/edit/{student.pk}/", {
			"name": "Lina Updated",
			"registration_number": "ST-003",
			"email": "lina.updated@example.com",
			"course": "Django REST Framework",
		})

		self.assertEqual(response.status_code, 302)
		student.refresh_from_db()
		self.assertEqual(student.name, "Lina Updated")
		self.assertEqual(student.email, "lina.updated@example.com")


class StudentDeleteViewTests(TestCase):
	def test_get_shows_confirmation_without_deleting_student(self):
		student = Student.objects.create(
			name="Lina",
			registration_number="ST-003",
			email="lina@example.com",
			course="Django",
		)

		response = self.client.get(f"/delete/{student.pk}/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Lina")
		self.assertTrue(Student.objects.filter(pk=student.pk).exists())

	def test_post_deletes_student_and_redirects_home(self):
		student = Student.objects.create(
			name="Lina",
			registration_number="ST-003",
			email="lina@example.com",
			course="Django",
		)

		response = self.client.post(f"/delete/{student.pk}/")

		self.assertRedirects(response, "/")
		self.assertFalse(Student.objects.filter(pk=student.pk).exists())
