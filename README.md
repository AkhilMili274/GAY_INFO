# Random Gay Status API

This project provides an API that returns a random "Gay" status based on a given username, age, and sex. The API checks the username against a predefined list and returns either "Yes" or "No" for the "Gay" status. Certain usernames are always marked as "not gay", while others are randomly assigned "Yes" or "No".

## Features

- The API returns a JSON response containing the `Username`, `Age`, `Sex`, and `"Gay"` status.
- Certain usernames, like "AKIRU", "I SHOW AKIRU", "AKHIL", and "AKHIL DAS", are always marked as `"Gay": "no"`.
- Other usernames are checked against a list, and if they match, the response will be `"Gay": "yes"`.
- For usernames not in the list, the response is randomly chosen between `"Gay": "yes"` or `"Gay": "no"`.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/random-gay-status-api.git
