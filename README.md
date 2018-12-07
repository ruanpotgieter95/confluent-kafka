# confluent-kafka
Examples in python and C# to connect to a kerberos SASL_PLAINTEXT cluster.

For python on linux you need to install librkafka & confluent-kafka:

wget https://rpmfind.net/linux/remi/fedora/29/remi/x86_64/librdkafka-devel-0.11.6-1.fc29.remi.x86_64.rpm
sudo dnf install librdkafka-devel-0.11.6-1.fc29.remi.x86_64.rpm
pip3 install --no-binary :all: confluent-kafka
