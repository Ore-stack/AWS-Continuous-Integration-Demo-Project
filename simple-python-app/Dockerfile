# Use the official Python 3.8 image as the base
FROM python:3.8

# Define the working directory within the container
WORKDIR /app

# Add the requirements file to the container
COPY requirements.txt .

# Install dependencies listed in the requirements file
RUN pip install -r requirements.txt

# Add the application code to the container
COPY . .

# Open port 5000 for the Flask app
EXPOSE 5000

# Optional: Set environment variables
# ENV MY_ENV_VAR=value

# Start the Flask application
CMD ["python", "app.py"]]
