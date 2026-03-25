import yaml
from processor import DataProcessor
from strategies import ConsoleOutput, RedisOutput, KafkaOutput, FirebaseOutput

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    mode = config.get("output_strategy", "console")
    
    if mode == "redis":
        strategy = RedisOutput(config['redis']['host'], config['redis']['port'])
    elif mode == "kafka":
        strategy = KafkaOutput(config['kafka']['bootstrap_servers'], config['kafka']['topic'])
    elif mode == "firebase":
        strategy = FirebaseOutput(config['firebase']['key_path'])
    else:
        strategy = ConsoleOutput()

    processor = DataProcessor(config['csv_file_path'], strategy)
    processor.execute()

if __name__ == "__main__":
    main()