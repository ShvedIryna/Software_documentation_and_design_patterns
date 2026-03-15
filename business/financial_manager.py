from data_access.models import Report

class FinancialManager:
    def __init__(self, repository, csv_reader):
        self.repository = repository
        self.csv_reader = csv_reader

    def process_data(self, file):
        data = self.csv_reader.read(file)

        total_income = sum(d.income for d in data)
        total_expense = sum(d.expense for d in data)

        report = Report(
            period="2025",
            totalIncome=total_income,
            totalExpense=total_expense,
            netProfit=total_income - total_expense
        )

        self.repository.save_financial_data(data)
        self.repository.save_report(report)

        return report