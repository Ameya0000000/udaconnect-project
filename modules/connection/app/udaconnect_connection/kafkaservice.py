from kafka import KafkaConsumer, KafkaProducer

class KafkaService:
    def __init__(self, kafka_topic):
        self.kafka_topic = kafka_topic
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def send_message(self, message):
        self.producer.send(self.kafka_topic, value=message)

    def consume_message(self):
        consumer = KafkaConsumer(self.kafka_topic,
                                 bootstrap_servers=['localhost:9092'])
        for message in consumer:
            print(message)
