{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e958dfa1-bebe-444b-b110-5fa8c0d9bc75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Student Performance Advisor\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your marks (out of 100):  72\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Performance Level: Good\n",
      "Suggestion: Focus on regular revision and practice.\n"
     ]
    }
   ],
   "source": [
    "print(\"Student Performance Advisor\")\n",
    "\n",
    "marks = int(input(\"Enter your marks (out of 100): \"))\n",
    "\n",
    "if marks >= 85:\n",
    "    print(\"Performance Level: Excellent\")\n",
    "    print(\"Suggestion: Keep up the great work and challenge yourself further.\")\n",
    "\n",
    "elif marks >= 60:\n",
    "    print(\"Performance Level: Good\")\n",
    "    print(\"Suggestion: Focus on regular revision and practice.\")\n",
    "\n",
    "elif marks >= 40:\n",
    "    print(\"Performance Level: Average\")\n",
    "    print(\"Suggestion: Spend more time understanding concepts and solving questions.\")\n",
    "\n",
    "else:\n",
    "    print(\"Performance Level: Needs Improvement\")\n",
    "    print(\"Suggestion: Seek help from teachers and make a study plan.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4021e403-8a36-43f8-a10b-3724c5b7a27b",
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
