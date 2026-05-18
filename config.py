"""Global Configuration for the Application"""
import os

SECRET_KEY = os.getenv("SECRET_KEY", "sup3r-s3cr3t")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///development.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
