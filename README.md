# LittleLemon REST API
Developed a RESTFUL API using Django Rest Framework(DRF), including Djoser for user validations.
Intergrated the Mysql database for security measurments, scabillity and robustness.
Authorized users can book tables and access protected messages.

### Features: 
- Retrive all the Menu items and create new item.
- Retrive a single Menu items, update items, and remove items.
- Retrive booked tables and insert new bookings.
- Retrive a single booking table, modify new bookings and delete it.
- Create an email, username, and password with Djoser.
- Implemented token generation using Django REST Framework (DRF) and configured login and logout endpoints with Djoser.
- UniTest Django built in test for validations and managing bugs.

### PATHS:
- http://127.0.0.1:8000/api/menu/ OR http://127.0.0.1:8000/api/menu/1
- http://127.0.0.1:8000/api/booking/ OR http://127.0.0.1:8000/api/booking/1
- http://127.0.0.1:8000/auth/users 
- http://127.0.0.1:8000/auth/token/login
- http://127.0.0.1:8000/auth/token/logout
- http://127.0.0.1:8000/api/message/
