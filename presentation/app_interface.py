from abc import ABC, abstractmethod


class IFinancialApp(ABC):

    @abstractmethod
    def run(self):
        pass