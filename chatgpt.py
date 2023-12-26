{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1ebce61e-110c-4c0e-8fd3-f1032dfc7b76",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8f832ace-82a4-45bf-add8-dada73ef42ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c9c73978-42b8-4733-bda7-d94e60836433",
   "metadata": {},
   "outputs": [],
   "source": [
    "import constants"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "03bc3aa3-2b85-49cb-8658-457079ba7636",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'constants' has no attribute 'APIKEY'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/4q/0htxzkld3w92xm82vcqmzndr0000gq/T/ipykernel_13995/3773125543.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menviron\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"OPENAI_API_KEY\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconstants\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mAPIKEY\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m: module 'constants' has no attribute 'APIKEY'"
     ]
    }
   ],
   "source": [
    "os.environ[\"OPENAI_API_KEY\"] = constants.APIKEY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32070506-dde8-4d6a-a093-8039280b4a90",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
