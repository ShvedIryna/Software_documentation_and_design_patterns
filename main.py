from processor import DataProcessor
from config import get_strategy
from strategies import *

if __name__ == "__main__":
    current_strategy = get_strategy()
    
    processor = DataProcessor(current_strategy)
    processor.process_csv("data.csv")