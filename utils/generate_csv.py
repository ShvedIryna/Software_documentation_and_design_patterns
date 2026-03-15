import csv
import random
from datetime import datetime, timedelta


def generate():

    start = datetime(2024, 1, 1)

    with open("financial_data.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["date", "income", "expense"])

        for i in range(1000):

            date = start + timedelta(days=i)

            income = random.randint(100, 1000)
            expense = random.randint(50, 900)

            writer.writerow([date.strftime("%Y-%m-%d"), income, expense])


if __name__ == "__main__":
    generate()