using Confluent.Kafka;
using System;
 
namespace KafkaDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            var bootstrapservers = "<HOSTNAME>:6667";
 
            var config = new ProducerConfig
            {
                BootstrapServers = bootstrapservers,
                MessageMaxBytes = 2097152,
                SecurityProtocol = SecurityProtocolType.Sasl_Plaintext,
                SaslMechanism = SaslMechanismType.Gssapi,
                SaslKerberosServiceName = "kafka"
            };
 
            var producer = new Producer<Null, string>(config);
            var brokerMessage = new Message<Confluent.Kafka.Null, string>()
            {
                Value = "Test Data"
            };
            var result = producer.ProduceAsync("<TOPIC_NAME>", brokerMessage).Result;
 
            Console.WriteLine(result.Value);
            Console.ReadLine();
        }
    }
}