
# Pipeline Purge 
This small script allow you to :

* Purge your pipeline's history using the API.

## Dependencies
* [Python](http://www.python.org/) v.3.1
* Python modules:
** Requests

To install them, on Debian/Ubuntu:

```
pip install requests 
```

## Configuration

Set the variable : 

- endpoint => URL of your gitlab (or put a Gitlab Variable)

From your gitlab instance create an API Token and put it as gitlab's variable named : API_TOKEN 

## Usage

Just push this to your gitlab repository and trigger the CI.

## Example Ouput from CI : 

```
python  gitlab-purge.py $API_TOKEN
Delete pipeline for Configuration Template
Pipeline 13349 deleted
Pipeline 13348 deleted
...
```

## Contributed by

Alexis TARUSSIO <alexis.tarussio@gmail.com>
