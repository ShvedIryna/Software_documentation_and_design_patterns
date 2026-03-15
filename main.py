from data_access.database import init_db
from data_access.repository_impl import FinancialRepository
from data_access.csv_reader import CSVReader
from business.financial_manager import FinancialManager
from business.chart_generator import ChartGenerator

def main():
    init_db()

    repository = FinancialRepository()
    csv_reader = CSVReader()
    manager = FinancialManager(repository, csv_reader)

    try:
        report = manager.process_data("financial_data.csv")

        chart = ChartGenerator()
        chart.generate_income_chart()
        chart.generate_expense_chart()

        print("\n" + "="*30)
        print(" FINANCIAL REPORT SUMMARY ")
        print("="*30)
        print(f"Period:        {report.period}")
        print(f"Total Income:  {report.totalIncome:,.2f}")
        print(f"Total Expense: {report.totalExpense:,.2f}")
        print(f"Net Profit:    {report.netProfit:,.2f}")
        print("="*30)

    except FileNotFoundError:
        print("Error: 'financial_data.csv' not found. Please run utils/generate_csv.py first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()