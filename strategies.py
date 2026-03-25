import redis
import json
import firebase_admin
from abc import ABC, abstractmethod
from kafka import KafkaProducer
from firebase_admin import credentials, firestore

class ShootingIncident:
    def __init__(self, incident_key, boro, occur_date):
        self.incident_key = incident_key
        self.boro = boro
        self.occur_date = occur_date

    def to_dict(self):
        return {
            "id": self.incident_key,
            "boro": self.boro,
            "date": self.occur_date
        }

    def __str__(self):
        return f"Incident ID: {self.incident_key} | Borough: {self.boro} | Date: {self.occur_date}"

class OutputStrategy(ABC):
    @abstractmethod
    def write(self, data):
        pass

class ConsoleOutput(OutputStrategy):
    def write(self, data):
        print("\n=== [STRATEGY: CONSOLE] ===")
        for item in data[:10]:
            print(item)
        print(f"Total processed: {len(data)} records.")

class RedisOutput(OutputStrategy):
    def __init__(self, host='localhost', port=6379):
        self.r = redis.Redis(host=host, port=port, decode_responses=True)

    def write(self, data):
        print("\n=== [STRATEGY: REDIS] ===")
        for item in data:
            self.r.set(f"nypd:{item.incident_key}", f"{item.boro} ({item.occur_date})")
        print(f"Successfully saved {len(data)} records to Redis.")

class KafkaOutput(OutputStrategy):
    def __init__(self, bootstrap_servers='localhost:9092', topic='nypd_shootings'):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def write(self, data):
        print("\n=== [STRATEGY: KAFKA] ===")
        for item in data:
            self.producer.send(self.topic, item.to_dict())
        self.producer.flush()
        print(f"Sent {len(data)} messages to Kafka topic: {self.topic}")

class FirebaseOutput(OutputStrategy):
    def __init__(self, key_path="serviceAccountKey.json"):
        if not firebase_admin._apps:
            cred = credentials.Certificate(key_path)
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def write(self, data):
        print("\n=== [STRATEGY: FIREBASE] ===")
        for item in data[:20]:
            doc_ref = self.db.collection("nypd_incidents").document(item.incident_key)
            doc_ref.set(item.to_dict())
            print(f"Uploaded to Cloud: {item.incident_key}")
        print("Check Firebase Console -> Firestore Database.")