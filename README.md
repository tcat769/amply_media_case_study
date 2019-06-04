##A Simple RESTful API
This RESTful API is a simple one that will return JSON detailing the weather description and high and low temparatures for your area when you hit the /weather endpoint.

###/weather endpoint
When you hit the /weather endpoint, I hit https://j9l4zglte4.execute-api.us-east-1.amazonaws.com/api/ctl/weather to grab weather data for your area, unless it is stored in a sqllite cache.  I then parse out the description and high and low temperatures for your area for the next 3 days and return just that information.
