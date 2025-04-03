{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64edaa93-051d-4518-95da-73dd6be1e741",
   "metadata": {},
   "outputs": [],
   "source": [
    "FROM python:3.9-slim\n",
    "\n",
    "WORKDIR /app\n",
    "\n",
    "COPY requirements.txt .\n",
    "RUN pip install --no-cache-dir -r requirements.txt\n",
    "\n",
    "COPY . .\n",
    "\n",
    "EXPOSE 8080\n",
    "\n",
    "CMD [\"python\", \"app.py\"]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
