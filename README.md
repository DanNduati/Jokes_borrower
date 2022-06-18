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
Run source.sh bash script
### Local sqlite database
```bash
$ ./source.sh 
Borrowing initiated
started borrowing at id 0
62 jokes borrowed successfully in 1.219724178314209 seconds
started borrowing at id 100
81 jokes borrowed successfully in 2.874145269393921 seconds
started borrowing at id 200
76 jokes borrowed successfully in 1.8248345851898193 seconds
All done
```
### Free tier hobby postgres instance
```bash
$ sudo chmod +x source.sh
$ ./source.sh
Borrowing initiated
started borrowing at id 0
62 jokes borrowed successfully in 34.831594467163086 seconds
started borrowing at id 100
81 jokes borrowed successfully in 43.83061122894287 seconds
started borrowing at id 200
76 jokes borrowed successfully in 41.592899322509766 seconds
All done
```
> For [obvious reasons](https://sj14.gitlab.io/post/2018/12-22-dbbench/) writing to the local sqlite database is significantly faster that writing to the free tier postgres database instance 
## <b>Built with</b>
- [aiohttp](https://docs.aiohttp.org/en/stable/) - an asynchronous HTTP Client/Server 
- [Tortoise orm](https://tortoise-orm.readthedocs.io/en/latest/index.html) - an asyncio ORM

## <b>Credit</b>
JokesBorrower sources it jokes from this [API](https://rapidapi.com/Sv443/api/jokeapi-v2/) created by [Sven Fehler](https://github.com/Sv443)

## <b>To do</b>
- [x] Throttle requests to avoid exceeding the request budget for rate limited APIs 
- [ ] Add other joke sources/Apis

## <b>License</b>
[![license](https://img.shields.io/badge/License-Beerware-yellowgreen)](LICENSE)
