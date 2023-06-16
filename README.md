# MetaBackendCapstone
The Capstone project enables you to demonstrate multiple skills by solving an authentic real-world problem. 

## API endpoints 
Api endpoints to test:

* http://127.0.0.1:8000/api/menu/
* http://127.0.0.1:8000/api/menu/{menuID}
* http://127.0.0.1:8000/api/restaurant/booking/tables/
* http://127.0.0.1:8000/api/restaurant/booking/tables/{tableID}/
* http://127.0.0.1:8000/api/api-token-auth/  to generate tokens for authentication

# Run project
Ensure to create a mysql database with the name in the settings and upsate the username and password as required
# Static Content

The address for serving the rendered static content is `127.0.0.1:8000/api/`.  Static assests are referenced and rendered through the template page `index.html`.

# Unit Testing

the tests file test_views and test_models is found in the tests folder in the project level directory
There are only two unit tests provided in this project.  They can be run using the following command: `python manage.py test tests`.

# API Endpoints
Endpoints that require an authentication token have been indicated in the table below.

| Endpoint | Method | Token Required | Client Payload | Expected Behavior |
| --- | --- | --- | --- | --- |
| _user creation and authentication_ |  |  |  |  |
| `/auth/users/` | POST | --- | `username`, `email`, `password` | Creates a new user account. Returns serialized `User` object data. |
| `/auth/token/login/` | POST | --- | `username`, `password` | Creates an authentication token for the given user.  Returns the generated token. |
| _menu items_ |  |  |  |  |
| `/api/menu-items/` | POST | yes | `title`, `price`, `inventory` | Creates new `MenuItem`.  Returns serialized data for `MenuItem` object. |
| `/api/menu-items/` | GET | yes | --- | Returns an array of serialzed `MenuItem` objects. |
| `/api/menu-items/<int:pk>` | GET | yes | --- | Returns serialzed `MenuItem` object with the corresponding id. |
| `/api/menu-items/<int:pk>` | PUT, PATCH | yes | `title`, `price`, `inventory` | Update `MenuItem` object with the corresponding id. |
| `/api/menu-items/<int:pk>` | DELETE | yes | --- | Remove `MenuItem` object with the corresponding id. |
| _booking_ |  |  |  |  |
| `/restaurant/bookings/tables/` | GET | yes | --- | Returns array of serialized `Booking` objects. |
| `/restaurant/bookings/tables/` | POST | yes | `name`, `no_of_guests`, `booking_date` | Reservers a table.  Returns serialized `Booking` object data. |
| _user creation and authentication_ |  |  |  |  |
| `/auth/token/logout/` | GET | yes | --- | Invalidates the token for the associated user.  Returns no payload. |