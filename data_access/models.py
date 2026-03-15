from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    userId = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)

    def login(self):
        print(f"{self.name} logged in")

    def logout(self):
        print(f"{self.name} logged out")


class FinancialData(Base):
    __tablename__ = "financial_data"

    dataId = Column(Integer, primary_key=True)
    date = Column(Date)
    income = Column(Float)
    expense = Column(Float)

    def calculateProfit(self):
        return self.income - self.expense


class Report(Base):
    __tablename__ = "reports"

    reportId = Column(Integer, primary_key=True)
    period = Column(String)
    totalIncome = Column(Float)
    totalExpense = Column(Float)
    netProfit = Column(Float)

    def generateReport(self):
        print("Report generated")

    def exportToPDF(self):
        print("Exporting report to PDF")