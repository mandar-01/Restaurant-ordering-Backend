# Use the official Python 3.11.2 image as the base image
FROM python:3.11.2

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install the dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Print the current directory contents for debugging
RUN ls -l

# Expose port 5000
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=.\\api\\index.py

# Print the content of FLASK_APP for debugging
RUN echo $FLASK_APP

# Run the Flask application with the specified command
CMD ["flask", "--app", "api.index", "--debug", "run", "--host", "0.0.0.0"]