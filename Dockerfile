# Use py3 base image
FROM python:3

# Set working dir
WORKDIR /app

# Copy current contents into container
COPY . /app

# Install deps
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 80
EXPOSE 80

# Define envs
ENV CLIENT_ID cef50287b44defde401b
ENV CLIENT_SECRET ebd6a6b67e160f9cbcdfe921a1dde47610edaa3f

CMD ["python3", "app.py"]
