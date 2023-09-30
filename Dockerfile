# Use the Selenium/standalone-chrome image as the base
FROM selenium/standalone-chrome:latest

# Set the working directory in the container
WORKDIR /app

# Install Python and Pip
USER root
RUN apt update -y && apt install -y python3 python3-pip

# Set the PATH environment variable
ENV PATH="/usr/local/bin:$PATH"

# Copy your project into the container
COPY . .

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy and give execute permission to the script
COPY exec_test.sh /exec_test.sh
RUN chmod +x /exec_test.sh

# Specify the entry point to run the script
CMD ["/exec_test.sh"]
