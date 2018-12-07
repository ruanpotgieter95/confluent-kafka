# confluent-kafka
Examples in python and C# to connect to a kerberos SASL_PLAINTEXT cluster.

# ***librkafka & confluent-kafka install***
```
***Use your package installer if not running fedora***

1. wget https://rpmfind.net/linux/remi/fedora/29/remi/x86_64/librdkafka-devel-0.11.6-1.fc29.remi.x86_64.rpm
2. sudo dnf install librdkafka-devel-0.11.6-1.fc29.remi.x86_64.rpm
3. pip install --no-binary :all: confluent-kafka
```
# ***Create a keytab***
```
1. ktutil
  a. addent -password -p {USERNAME}@{DOMAIN} -k 1 -e RC4-HMAC
  b. wkt {KEYTABNAME}.keytab
2. klist -kte {KEYTABNAME}.keytab
3. kinit -kt {KEYTABNAME}.keytab {USERNAME}@{DOMAIN}
```

# ***Export***
```
export KAFKA_CLIENT_KERBEROS_PARAMS="-Djava.security.auth.login.config=/usr/hdp/current/kafka-broker/config/kafka_client_jaas.conf"
```
