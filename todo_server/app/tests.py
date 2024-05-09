from datetime import datetime, timedelta

from rest_framework.test import APITestCase

from . import models


class TaskTests(APITestCase):
    def setUp(self) -> None:
        self.task1 = models.Task.objects.create(
            title="Task 1",
            priority=models.Task.Priority.LOW,
        )
        return super().setUp()

    def test_list_tasks(self):
        res = self.client.get("/tasks/")
        data = res.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        task_data = data[0]
        self.assertIsInstance(task_data, dict)
        self.assertListEqual(
            list(task_data.keys()),
            ["id", "title", "priority", "due_on", "status", "created_on"],
        )
        # print(data)

    def test_get_task(self):
        res = self.client.get(f"/tasks/{self.task1.pk}/")
        data = res.json()
        self.assertIsInstance(data, dict)
        self.assertListEqual(
            list(data.keys()),
            ["id", "title", "priority", "due_on", "status", "created_on"],
        )
        # print(data)

    def test_create_task(self):
        tomorrow = datetime.now() + timedelta(days=1)
        json_data = {
            "title": "Task 2",
            "priority": models.Task.Priority.HIGH,
            "due_on": tomorrow.isoformat(),
        }
        res = self.client.post("/tasks/", json_data, format="json")
        data = res.json()

        self.assertIsInstance(data, dict)
        self.assertEqual(data["title"], "Task 2")

        self.assertEqual(models.Task.objects.count(), 2)
        # print(data)

    def test_update_task(self):
        # Make sure the initial data is correct
        self.assertEqual(self.task1.priority, models.Task.Priority.LOW)
        self.assertEqual(self.task1.status, models.Task.Status.NOT_STARTED)

        json_data = {
            "priority": "HIGH",
            "status": "IN_PROGRESS",
        }
        self.client.patch(f"/tasks/{self.task1.pk}/", json_data, format="json")

        # Check the Task object was updated
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.priority, models.Task.Priority.HIGH)
        self.assertEqual(self.task1.status, models.Task.Status.IN_PROGRESS)

    def test_delete_task(self):
        self.client.delete(f"/tasks/{self.task1.pk}/")
        self.assertEqual(models.Task.objects.count(), 0)
