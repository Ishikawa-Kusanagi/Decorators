import datetime
from functools import wraps

import requests


def my_func(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        try:
            result = old_function(*args, **kwargs)

            if result.status_code == 200:
                data = result.json()

                with open('character.txt', 'a') as file:
                    file.write(f"{datetime.datetime.now()}: {data}\n")
            else:
                with open('character.txt', 'a') as file:
                    file.write(
                        f"{datetime.datetime.now()}: Error {result.status_code} for URL {result.url}\n")

            return result

        except Exception as e:
            with open('character.txt', 'a') as file:
                file.write(
                    f"{datetime.datetime.now()}: Exception occurred: {str(e)}\n")
            raise e

    return new_function


@my_func
def swapi(people_id):
    return requests.get(f'https://swapi.dev/api/people/{people_id}')


response = swapi(1)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
