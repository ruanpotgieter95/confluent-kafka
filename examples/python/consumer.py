from confluent_kafka import Consumer, KafkaError
 
c = Consumer({
    'bootstrap.servers': '<HOSTNAME>:6667',
    'auto.offset.reset': 'earliest',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanism': 'GSSAPI',
    'sasl.kerberos.service.name': 'kafka',
    'group.id': 'mygroup'
})
 
c.subscribe(['<TOPIC_NAME>'])
 
while True:
    msg = c.poll(1.0)
 
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break
 
    print('Received message: {}'.format(msg.value().decode('utf-8')))
 
c.close()
