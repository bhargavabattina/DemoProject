# Use official Python image with newer Node.js
FROM python:3.9-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Install system dependencies and Node.js 20.x
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    git \
    ca-certificates \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*



# Install Playwright and browsers
RUN pip install --upgrade pip && \
    pip install playwright && \
    playwright install && \
    playwright install-deps



# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install allure-pytest pytest-playwright

# Copy the rest of the application
COPY . .

# Run tests and generate Allure reports
CMD pytest --alluredir=allure-results && allure generate allure-results --clean -o allure-report

# Command to run tests and generate report
CMD ["sh", "-c", \
     "pytest --alluredir=allure-results && \
     allure generate allure-results -o allure-report --clean && \
     cp allure-plugin/custom-title-plugin/custom.css allure-report/ && \
     sed -i '/<\\/head>/i <link rel=\"stylesheet\" type=\"text/css\" href=\"custom.css\">' allure-report/index.html && \
     sed -i 's|<title>Allure Report</title>|<title>Orange HRM Report</title>|' allure-report/index.html"]