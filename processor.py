import csv
from strategies import ShootingIncident

class DataProcessor:
    def __init__(self, file_path, strategy):
        self.file_path = file_path
        self.strategy = strategy

    def execute(self):
        incidents = []
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    incidents.append(ShootingIncident(
                        row.get('INCIDENT_KEY', 'N/A'),
                        row.get('BORO', 'N/A'),
                        row.get('OCCUR_DATE', 'N/A')
                    ))
            if incidents:
                self.strategy.write(incidents)
        except FileNotFoundError:
            print(f"Error: {self.file_path} not found.")