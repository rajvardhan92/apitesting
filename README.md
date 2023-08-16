# API Automation Framework

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![PyTest](https://img.shields.io/badge/pytest-passing-brightgreen.svg)

This repository contains a Python-based API automation framework for testing the Restful Booker API. The framework is designed to streamline API testing processes and provide reliable test coverage for various endpoints.

## Features

- Easily create, read, update, and delete bookings using well-organized test methods.
- Automated token generation for authentication using provided credentials.
- Utilizes the popular Requests library for sending API requests.
- PyTest framework ensures clear test execution and reporting.

## Getting Started

### Prerequisites

- Python 3.x
- Requests library (install using `pip install requests`)
- PyTest library (install using `pip install pytest`)

### Setup

1. Clone this repository to your local machine.
2. Navigate to the repository directory:

cd API-Automation-Framework


### Usage

1. Update the authentication credentials in the `TestRestfulBookerAPI` class (`username` and `password`).
2. Modify the base URL (`base_url`) if needed.
3. Run the tests using PyTest:

pytest your_test_script_name.py

### Test Cases

- `test_create_booking`: Creates a booking and verifies that the response status code is 200 (OK).
- `test_get_booking`: Creates a booking, retrieves it using the booking ID, and checks the response status code.
- `test_update_booking`: Creates a booking, updates it with new data, and verifies the response status code.
- `test_delete_booking`: Creates a booking, deletes it, and ensures the booking is no longer retrievable.

## Contributing

Contributions are welcome! If you find bugs or want to improve the framework, feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
