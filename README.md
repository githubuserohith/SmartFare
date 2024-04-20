# SmartFare

# Facial Recognition and Fare Automation System

## Overview
This Django project implements a system for public transportation that leverages facial recognition technology for passenger identification and automatic fare deduction. 

## Features
- **User Registration**: Users can register by providing their username, email, and password.
  
![alt text](https://imgur.com/CnaXZY6.png)

- **Facial Recognition**: Utilizes facial recognition technology to identify passengers.
  
  ![alt text](https://imgur.com/0mho9nJ.png)
  
- **Automatic Fare Deduction**: Fares are automatically deducted from passengers' accounts once their identity is verified.
  
  ![alt text](https://imgur.com/ZfV3aZm.png)
  
- **Wallet Management**: Users can view their wallet balance and add funds as needed.
 
  ![alt text](https://imgur.com/oMXYTLd.png)
  
- **Admin Panel**: Administrators have access to features like starting and ending boarding sessions, calculating fare durations, and managing payments.
  
  ![alt text](https://imgur.com/q3pF9Dc.png)
  
- **OTP Authentication**: Implements OTP-based authentication for login and password recovery.
  
 ![alt text](https://imgur.com/b5JWrkH.png)
  
- **Bot Integration**: Includes a chatbot feature for admin interaction.
  
![alt text](https://imgur.com/j1bVbvB.png)

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up environment variables:
    - Set `stripe_secret_key` and `stripe_pub_key` in your environment variables.
    - Set up Gmail credentials for sending OTP emails.

## Usage
1. Run migrations:
    ```bash
    python manage.py migrate
    ```
2. Start the development server:
    ```bash
    python manage.py runserver
    ```
3. Access the application at `http://localhost:8000`.

## Contributing
Contributions are welcome! Please open an issue to discuss proposed changes or submit a pull request directly.
