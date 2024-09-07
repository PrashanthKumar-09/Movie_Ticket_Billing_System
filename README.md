# Movie Ticket Booking System

## Project Overview
The **Movie Ticket Booking System** is a simple Python-based console application designed to help users book movie tickets. This project aims to demonstrate basic Python programming concepts such as functions, loops, conditionals, and file handling, while also simulating a real-world use case.

## Features
- **Movie List**: Users can view available movies and showtimes.
- **Ticket Booking**: Users can select a movie, choose the number of tickets, and confirm their booking.
- **Seat Selection**: Allows users to select specific seats (if implemented).
- **Payment Gateway Simulation**: A mock payment gateway simulates the process of paying for tickets.
- **Ticket Confirmation**: After payment, users receive a booking confirmation with ticket details.
- **User-friendly Interface**: The application is run on the command line with easy-to-navigate menus.

## Technologies Used
- **Python 3.x**: The entire application is built using Python, leveraging basic libraries like `datetime`, `random`, and `sys`.
- **File Handling**: Booking history and available movies may be stored in `.txt` or `.csv` files (depending on your implementation).
- **Error Handling**: The application handles common errors such as invalid inputs and unavailable seats.


## How to Use
1. Upon running the script, you will be greeted with a menu displaying available movies.
2. Select a movie and the number of tickets you want to book.
3. If seat selection is implemented, you will be asked to choose your seats.
4. After confirming your selection, you will be prompted to proceed to payment.
5. Once payment is confirmed, your booking details will be displayed and saved.

## Future Enhancements
- **Graphical User Interface (GUI)**: Add a GUI using libraries like `Tkinter` or `PyQt`.
- **Database Integration**: Implement a database (e.g., SQLite) to store user bookings and movie information.
- **Advanced Payment Gateway**: Integrate with real payment APIs for processing payments.
- **Notifications**: Send email confirmations using `smtplib`.
