from abc import ABC, abstractmethod


class IFinancialRepository(ABC):

    @abstractmethod
    def save_financial_data(self, data):
        pass

    @abstractmethod
    def save_report(self, report):
        pass