# password-validator-api
A GraphQL api to validate passwords
<br>
To run you need install the packages: pip install -r requirements.txt
<br>
You can run directly on your terminal or using the Dockerfile
<br>
<h4>Terminal</h4>
<br>
Run: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
<br>
<h4>Dockerfile</h4>
<br>
Run: dockerbuild -t password_validator .
<br>
Run: docker run -d --name password_container -p 8000:8000 password_validator
<br>
<h3>Testing the API</h3>
<br>
Test the api on this link: <br>
<a href="http://localhost:8000/graphql">http://localhost:8000/graphql</a>
<br>
It is the GraphQL Playground.

<h3>Testing the application</h3>
<br>
I have used pytest to run several tests on the application. You can see the tests on the folder /tests .
<br>
Run the tests by typing the command line: pytest 

