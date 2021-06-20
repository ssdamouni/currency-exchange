# Conceptual Exercise

Answer the following questions below:

## What are important differences between Python and JavaScript?
    The differences in syntax are probably the most immediately obvious. Python's of white space is vital the way the code is actually run. First depending on where indentation is used can change which parts of the code go with which. In addition, there is only one type of variable in python and you don't have to use a variable keyword. Javascript tends has three different ways to declare variables and each one is good for different cirmcumstances. Indentation in Javascript is used primarily to make your code more readable but doens't affect how the code runs. In a broad sense Python tends to lend itself better to backend development and working with data structures and Javascript is better for creating dyanamic webpages. 

## Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you can try to get a missing key (like "c") *without* your programming crashing.
    dict = {"a": 1, "b": 2}
    dic.get("c", "default value"), if c exists it will return the correct value otherise it will return the default value

    import collections
    dict = collections.defaultdict(lambda: 'Key not Present'), this would return "key not present" for any missing keys

## What is a unit test?
    Unit tests are tests small one small part of your application. Usually just individual functions to show how they work and that 
  they work properly. 

## What is an integration test?
    Integration tests are tests that focus on how different functions work together to make the application work.

## What is the role of web application framework, like Flask?
    Makes creating a website that relies are a server easy and fast. It also allows the devolper to use to templates and 
  help create a lot different pages quickly. It does this by having specific logic to accept and handle all types of requests
  depending on what the user wants.   

## You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
    A parameter usually references a specific resources on the backend. The query string is 
  usually used to filter or sort the resources on the backend.

## How do you collect data from a URL placeholder parameter using Flask?
    You add the placeholder in brackets within the url. 'route/<placeholder>' for example. The you pass the variable into the routing function.

## How do you collect data from the query string using Flask?
  To collect data from the query string you use request.args["what every key you want the value for"]

## How do you collect data from the body of the request using Flask?
  You send the form to the route you are going to use the data in. Then you can use request.data or request.args

## What is a cookie and what kinds of things are they commonly used for?
    A cookie are small pieces of information that are stored on the client side in the browser but
  can also be sent to a server along with a request. There are often used for authenticating users and
  keeping track of shopping carts on e-commerce sights. 

## What is the session object in Flask?
    Session is a tool in Flask that is built on top of cookies. It essentailly gives web apps state. So sessions can keep track of
  information, read the information and alter the information.

## What does Flask's `jsonify()` do?
  It turns the JSON output into a Response object with the application/json. For convenience, it also converts multiple arguments into an array or multiple keyword arguments into a dictionary.
