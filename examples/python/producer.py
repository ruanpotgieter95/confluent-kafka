from confluent_kafka import Producer
 
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))
 
 
p = Producer({
    'bootstrap.servers': '<HOSTNAME>:6667',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanism': 'GSSAPI',
    'sasl.kerberos.keytab': '<KEYTABNAME>.keytab',
    'sasl.kerberos.service.name': 'kafka',
})
 
try:
    for val in range(1, 1000):
        p.produce('<TOPIC_NAME>', 'myvalue #{0}'
                  .format(val), callback=acked)
        p.poll(0.5)
 
except KeyboardInterrupt:
    pass
