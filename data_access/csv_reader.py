import csv
from datetime import datetime
from data_access.models import FinancialData


class CSVReader:

    def read(self, file):

        result = []

        with open(file) as f:

            reader = csv.DictReader(f)

            for row in reader:

                data = FinancialData(
                    date=datetime.strptime(row["date"], "%Y-%m-%d"),
                    income=float(row["income"]),
                    expense=float(row["expense"])
                )

                result.append(data)

        return result