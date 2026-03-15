from data_access.repository_interface import IFinancialRepository
from data_access.database import SessionLocal

class FinancialRepository(IFinancialRepository):

    def save_financial_data(self, data):
        session = SessionLocal()
        try:
            for d in data:
                session.add(d)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error saving financial data: {e}")
        finally:
            session.close()

    def save_report(self, report):
        session = SessionLocal()
        try:
            session.add(report)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error saving report: {e}")
        finally:
            session.close()