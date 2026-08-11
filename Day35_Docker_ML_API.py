# ==========================================================
# DAY 35 - DOCKER + FASTAPI ML API
# ==========================================================


# ==========================================================
# Q1. What is Docker?
# ==========================================================

# Docker is a platform used to package an application,
# its dependencies, libraries and configuration into
# a portable container.


# ==========================================================
# Q2. Create a simple Python test file
# ==========================================================

print("ML API Docker Container is running!")


# ==========================================================
# Q3. Check Python Version
# ==========================================================

import sys

print(
    "Python Version:",
    sys.version
)


# ==========================================================
# Q4. Check Installed Packages
# ==========================================================

import pandas
import sklearn
import fastapi

print(
    "Pandas:",
    pandas.__version__
)

print(
    "Scikit-learn:",
    sklearn.__version__
)

print(
    "FastAPI:",
    fastapi.__version__
)


# ==========================================================
# Q5. Environment Information
# ==========================================================

print(
    "Application is ready to run inside Docker."
)


# ==========================================================
# END OF DAY 35
# ==========================================================
