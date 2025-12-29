{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "750bf348-fa00-411b-92a4-99b3bec760e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the length of side 1:  68\n",
      "enter the length of side 2:  68\n",
      "enter the length of side 3:  90\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "it is an isoceles triangle\n"
     ]
    }
   ],
   "source": [
    "side1 = float(input(\"enter the length of side 1: \"))\n",
    "side2 = float(input(\"enter the length of side 2: \"))\n",
    "side3 = float(input(\"enter the length of side 3: \"))\n",
    "if side1 == side2 == side3:\n",
    "    print(\"it is an equalateral triangle.\")\n",
    "elif side1 == side2 or side1 == side3 or side2 == side3:\n",
    "    print(\"it is an isoceles triangle\")\n",
    "else:print(\"it is a scalene triangle\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d59fe20-f487-4f05-8f4d-bc2961ad96b5",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
