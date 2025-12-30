{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "81433eca-8338-46eb-bdd8-31df28a9cb35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How many subjects?  3\n",
      "Enter subject name:  Maths\n",
      "Difficulty (1-easy, 2-medium, 3-hard):  3\n",
      "Enter subject name:  Physics\n",
      "Difficulty (1-easy, 2-medium, 3-hard):  2\n",
      "Enter subject name:  Chemistry\n",
      "Difficulty (1-easy, 2-medium, 3-hard):  1\n"
     ]
    }
   ],
   "source": [
    "subjects = []\n",
    "\n",
    "n = int(input(\"How many subjects? \"))\n",
    "\n",
    "for i in range(n):\n",
    "    name = input(\"Enter subject name: \")\n",
    "    difficulty = int(input(\"Difficulty (1-easy, 2-medium, 3-hard): \"))\n",
    "    subjects.append((name, difficulty))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8a0ad40a-557d-4e01-966a-331ab76783e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "📚 Study Priority:\n",
      "Maths\n",
      "Physics\n",
      "Chemistry\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n📚 Study Priority:\")\n",
    "for subject in sorted(subjects, key=lambda x: x[1], reverse=True):\n",
    "    print(subject[0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef5ba954-9969-429c-ac59-e46b9343580e",
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
