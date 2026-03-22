from abc import ABC, abstractmethod

class OutputStrategy(ABC):
    @abstractmethod
    def send(self, data: dict):
        pass

class ConsoleStrategy(OutputStrategy):
    def send(self, data: dict):
        print(f"[CONSOLE] Recording Incident: {data.get('INCIDENT_KEY')} at {data.get('OCCUR_DATE')}")

class KafkaStrategy(OutputStrategy):
    def send(self, data: dict):
        print(f"[KAFKA] Sending to topic 'nypd_events': {data.get('INCIDENT_KEY')}")

class RedisStrategy(OutputStrategy):
    def send(self, data: dict):
        print(f"[REDIS] SET incident:{data.get('INCIDENT_KEY')} {data.get('STATISTICAL_MURDER_FLAG')}")