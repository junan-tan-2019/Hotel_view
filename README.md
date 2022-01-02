# Hotel View
Hotel view service for CS301 project. This is designed for the purpose of presenting a simple user interface demo, not a full-fledge service nor it is a production-ready service.
Requires data pulling from Ascendas hotel endpoints (No guarantee that it is available for pulling in the future.). Developed using Bootstrap 5, CSS, JavaScript, and
Jinja 2 with Flask framework. List of hotels are created using Pagination.js: https://pagination.js.org/

## This service consist of:

- Index.html:
  - A list of viewable hotels, which each button navigates the user to hotel.html that renders the selected hotel.
  
- Hotel.html:
  - A hotel showing list of hotel items, descriptions and list of available rooms for booking.
  
- room.html:
  - A specific room showing the price and other room details. Booking button is suppose to link to another service which is not available. This is for viewing purpose only. 
