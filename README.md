To complete the coding challenge, I made use of the Email Hunter API as well as the requests python library. At the beginning of the challenge, I attempted to solve the problem by implementing a web crawler myself, but after learning that I could use an external API, I did some research and found the Email Hunter API. 

The job that the API provides matches the problem of the challenge perfectly. Given a domain name, this API returns you a list of emails found for that domain name. By incorporating this API in to my code, I was able to send a get request to a specific endpoint (done by using the python requests library) with specific parameters, and search through the response given by the API for the emails returned. 

To run my script, you need to install the python requests library. This can be done using python’s pip and running the command “pip install requests” in the terminal. To use the API, I created an account, obtained the API key, and found out what kind of request I needed to send with what parameters. 

Upon running the code, you will be given a prompt to enter a domain name after which the emails found for that domain name will be printed. 