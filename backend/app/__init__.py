from flask import Flask
import connexion

app = connexion.FlaskApp(__name__)

from app import usersData
