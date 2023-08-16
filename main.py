import requests
import pytest


class TestRestfulBookerAPI:
    base_url = "https://restful-booker.herokuapp.com"
    username = "admin"
    password = "password123"

    """
     This class defines a set of test cases to validate the functionality of the Restful Booker API.
     It includes methods to create, get, update, and delete bookings, using various API endpoints.
     """

    @classmethod
    def setup_class(cls):
        cls.token = cls.generate_token()

        """
            This class method is executed before any test cases start running.
            It generates an authentication token using the provided credentials.
            """

    @classmethod
    def generate_token(cls):
        url = f"{cls.base_url}/auth"
        payload = {
            "username": cls.username,
            "password": cls.password
        }
        response = requests.post(url, json=payload)
        return response.json()["token"]

    """
           Generates an authentication token by sending a POST request to the authentication endpoint.
           Returns the token extracted from the response JSON.
           """

    def create_booking(self, data):
        url = f"{self.base_url}/booking"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={self.token}"
        }
        response = requests.post(url, json=data, headers=headers)
        return response

    def get_booking(self, booking_id):
        url = f"{self.base_url}/booking/{booking_id}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={self.token}"
        }
        response = requests.get(url, headers=headers)
        return response

    def update_booking(self, booking_id, data):
        url = f"{self.base_url}/booking/{booking_id}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={self.token}"
        }
        response = requests.put(url, json=data, headers=headers)
        return response

    def delete_booking(self, booking_id):
        url = f"{self.base_url}/booking/{booking_id}"
        headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={self.token}"
        }
        response = requests.delete(url, headers=headers)
        return response

    def test_create_booking(self):
        data = {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-08-01",
                "checkout": "2023-08-05"
            },
            "additionalneeds": "Breakfast"
        }
        response = self.create_booking(data)
        assert response.status_code == 200

    """
           Test case to validate the creation of a booking.
           Sends a POST request to the booking creation endpoint with sample data.
           Asserts that the response status code is 200 (OK).
           """

    def test_get_booking(self):
        # Create a booking and get its ID
        data = {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-08-01",
                "checkout": "2023-08-05"
            },
            "additionalneeds": "Breakfast"
        }
        create_response = self.create_booking(data)
        booking_id = create_response.json()["bookingid"]

        """
                Test case to validate the retrieval of a booking.
                Creates a booking and then sends a GET request to retrieve the created booking using its ID.
                Asserts that the response status code is 200 (OK).
                """

        # Get the created booking
        response = self.get_booking(booking_id)
        assert response.status_code == 200

    def test_update_booking(self):
        # Create a booking and get its ID
        """
                Test case to validate the updating of a booking.
                Creates a booking, then sends a PUT request to update the booking with new data.
                Asserts that the response status code is 200 (OK).
                """
        data = {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-08-01",
                "checkout": "2023-08-05"
            },
            "additionalneeds": "Breakfast"
        }
        create_response = self.create_booking(data)
        booking_id = create_response.json()["bookingid"]

        # Update the booking
        update_data = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        response = self.update_booking(booking_id, update_data)
        assert response.status_code == 200

    def test_delete_booking(self):
        # Create a booking and get its ID
        """
                Test case to validate the deletion of a booking.
                Creates a booking, then sends a DELETE request to delete the created booking using its ID.
                Asserts that the response status code is 201 (Created) for successful deletion.
                Also, verifies that the booking has been deleted by sending a GET request with the same ID.
                """
        data = {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-08-01",
                "checkout": "2023-08-05"
            },
            "additionalneeds": "Breakfast"
        }
        create_response = self.create_booking(data)
        booking_id = create_response.json()["bookingid"]

        # Delete the booking
        response = self.delete_booking(booking_id)
        assert response.status_code == 201

        # Verify the booking has been deleted
        get_response = self.get_booking(booking_id)
        assert get_response.status_code == 404


if __name__ == "__main__":
    pytest.main(["-s", "your_test_script_name.py"])
