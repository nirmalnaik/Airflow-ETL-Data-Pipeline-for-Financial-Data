# Use the official Airflow image as a base
FROM apache/airflow:2.9.0

# Switch to the Airflow user
USER airflow

# Install additional Python packages
RUN pip install matplotlib

# Switch back to root if you have any further root commands, otherwise, this line is not necessary
USER root
