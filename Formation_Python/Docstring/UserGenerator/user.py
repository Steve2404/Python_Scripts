"""Module to generate random users"""
import faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent # recuparation du chemin absolu de notre fichier
logging.basicConfig(filename=BASE_DIR/"user.log", level=logging.INFO)
fake = faker.Faker(locale="de_DE")

def get_user():
    """Generate a single user's name

    Returns:
        str: user
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(number_user):
    """Generate a list of user's names

    Args:
        number_user (int): number of user to generate

    Returns:
        list[str]: users
    """
    user = []
    for _ in range(number_user):
        user.append(get_user())
    logging.info(f"Generating a list of {number_user} user.")
    return user
    #return [get_user for _ in range(number_user)]



if __name__ == "__main__":
    print(get_users(5))
    