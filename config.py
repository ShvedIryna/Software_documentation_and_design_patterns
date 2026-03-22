import yaml
from strategies import ConsoleStrategy, KafkaStrategy, RedisStrategy

def get_strategy():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    method = config.get("output_method")
    
    if method == "kafka":
        return KafkaStrategy()
    elif method == "redis":
        return RedisStrategy()
    
    return ConsoleStrategy()