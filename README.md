<h1 align="center"><b>JokesBorrower</b></h1>
<h4 align="center"><b>JokesApi Robin Hood</b></h4>
<br>

The JokeBorrower as the name suggests ~~steals~~ cough I mean `sources` for jokes from other APIs to be used by my [jokesAPI](https://github.com/DanNduati/Jokes_api) by storing them to my heroku postgres database instance.  

## <b>Prerequisites</b>
- [Python3](https://www.python.org/downloads/)

## <b>Setup</b>
### <b>Clone repository</b>
```bash
$ git clone https://github.com/DanNduati/Jokes_borrower.git
```
### <b>Install dependencies</b>
If you have [pipenv](https://pipenv.pypa.io/) installed you can just run pipenv automatically creates a virtual environment for you:
```bash
$ pipenv install
```
Otherwise you can use the good ol' requirements.txt file:
```bash
# create virtualenvironment and activate it
$ python -m venv venv
$ source venv/bin/activate
# install dependencies
$ pip install -r requirements.txt
```
## <b>Usage</b>
```bash
$ python main.py 
100 jokes borrowed successfully in 1.018240594863892 seconds
```
100 requests and DB writes in about 1 second! How:
## <b>Built with</b>
- [aiohttp](https://docs.aiohttp.org/en/stable/) - an asynchronous HTTP Client/Server 
- [Tortoise orm](https://tortoise-orm.readthedocs.io/en/latest/index.html) - an asyncio ORM

## <b>Credit</b>
JokesBorrower sources it jokes from this [API](https://rapidapi.com/Sv443/api/jokeapi-v2/) created by [Sven Fehler](https://github.com/Sv443)

## <b>To do</b>
- Throttle requests to avoid exceeding the request budget for rate limited APIs 
- Add other joke sources/Apis

## <b>License</b>
[![license](https://img.shields.io/badge/License-Beerware-yellowgreen)](LICENSE)