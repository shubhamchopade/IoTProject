import os
import random
import time

# Set the duration of the data generation
duration = 5 * 60 * 60  # 5 hours in seconds

start_time = time.time()

while (time.time() - start_time) < duration:
    # ----------------------------------------------Station 1--------------------------------------
    # Generate random values for each sensor in the station 1
    n = random.randint(0, 30)
    p = random.randint(0, 30)
    k = random.randint(0, 30)
    temperature = random.randint(0, 12)
    humidity = random.randint(0, 30)
    ph = random.uniform(2, 4)
    rainfall = random.randint(0, 200)

    # Temperature Sensor
    temp1 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "Tffv9xUCkqtJOfyK0GS6" -m {{"temperature":{temperature}}}'
    os.system(temp1)

    # Humidity Sensor
    humidity1 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "roXlFMXKpDuNwuR5OLIu" -m {{"humidity":{humidity}}}'
    os.system(humidity1)

    # Ph Sensor
    ph1 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "rPC75iZ71GU623r7nJRf" -m {{"ph":{ph}}}'
    os.system(ph1)

    # Rainfall Sensor
    rainfall1 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "U3jedvKjBLOGvbRH9QlU" -m {{"rainfall":{rainfall}}}'
    os.system(rainfall1)

    # N Sensor
    n1 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "9Lnf9DkhuTu6IY9MBSAX" -m {{"n":{n}}}'
    os.system(n1)

    # P Sensor
    p1 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "PP5Waik4clK5uJluxyqQ" -m {{"p":{p}}}'
    os.system(p1)

    # K Sensor
    k1 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "G9BbLhig7MknVDShU2o9" -m {{"k":{k}}}'
    os.system(k1)


    # ----------------------------------------------Station 2--------------------------------------
    # Generate random values for each sensor in the station 2

    n = random.randint(30, 60)
    p = random.randint(30, 60)
    k = random.randint(30, 60)
    temperature = random.randint(12, 24)
    humidity = random.randint(30, 60)
    ph = random.uniform(4, 6)
    rainfall = random.randint(200, 300)

    # Temperature Sensor
    temp2 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "n7Z8lCp7pbK6nSj5Xkkk" -m {{"temperature":{temperature}}}'
    os.system(temp2)

    # Humidity Sensor
    humidity2 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "zx3jtZxVhkuxWeqibO6Q" -m {{"humidity":{humidity}}}'
    os.system(humidity2)

    # Ph Sensor
    ph2 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "8Rv4rnTjUr72phVsrg3S" -m {{"ph":{ph}}}'
    os.system(ph2)

    # Rainfall Sensor
    rainfall2 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "2wv03HDI75JhIAgXIhwk" -m {{"rainfall":{rainfall}}}'
    os.system(rainfall2)

    # N Sensor
    n2 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "8XKoskl2u9VYUXpv0NwB" -m {{"n":{n}}}'
    os.system(n2)

    # P Sensor
    p2 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "a87MbzzrZk3SkPTjze7G" -m {{"p":{p}}}'
    os.system(p2)

    # K Sensor
    k2 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "Oz0iw7umetK616YR1aCs" -m {{"k":{k}}}'
    os.system(k2)


    # ----------------------------------------------Station 3--------------------------------------
    # Generate random values for each sensor in the station 3

    n = random.randint(60, 100)
    p = random.randint(60, 100)
    k = random.randint(60, 100)
    temperature = random.randint(25, 36)
    humidity = random.randint(60, 100)
    ph = random.uniform(7, 9)
    rainfall = random.randint(300, 400)

    # Temperature Sensor
    temp3 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "WVLgAdRByggLojsI1bmp" -m {{"temperature":{temperature}}}'
    os.system(temp3)

    # Humidity Sensor
    humidity3 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "ARDwBbcMzokdCNm7su37" -m {{"humidity":{humidity}}}'
    os.system(humidity3)

    # Ph Sensor
    ph3 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "gZgbvQZgkPZfnWEpaheV" -m {{"ph":{ph}}}'
    os.system(ph3)

    # Rainfall Sensor
    rainfall3 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "zCV69AtVOyJdzjzuhkoe" -m {{"rainfall":{rainfall}}}'
    os.system(rainfall3)

    # N Sensor
    n3 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "WnXqFFk5tUfsTzz0O9AB" -m {{"n":{n}}}'
    os.system(n3)

    # P Sensor
    p3 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "WBWPOZAUOf59I2qsh7xS" -m {{"p":{p}}}'
    os.system(p3)

    # K Sensor
    k3 = f'mosquitto_pub -d -q 1 -h "thingsboard.cloud" -p "1883" -t "v1/devices/me/telemetry" -u "2NqHQ5LMUTKLuzgGMjOl" -m {{"k":{k}}}'
    os.system(k3)



    # Time between each message
    time.sleep(10)