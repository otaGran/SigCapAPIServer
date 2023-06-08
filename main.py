from flask import Flask, request, jsonify
import psycopg2

import jsonschema
import json

with open('schema.json') as f:
    schema = json.load(f)
import json

app = Flask(__name__)
with open("pass.json", 'r') as file:
    credential = json.load(file)

# Database connection configuration
db_host = credential['db_host']
db_port = credential['db_port']
db_name = credential['db_name']
db_user = credential['db_user']
db_password = credential['db_password']


@app.route('/api/data', methods=['POST'])
def receive_data():
    # Get the JSON data from the request
    data = request.get_json()
    print(data)

    with open('schema.json') as f:
        schema = json.load(f)

    try:
        jsonschema.validate(instance=data, schema=schema)

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)
        cursor = conn.cursor()

        # Convert the JSON data to a string

        for item in data:
            # Execute the INSERT query
            cursor.execute("INSERT INTO \"SigCapDetails\" (\"deviceID\", \"operatorID\",\"batchUUID\",\"recordTimeStamp\",azimuth,pitch,roll,longitude, latitude, altitude, \"mRegistered\", "
                           "\"mTimeStamp\", \"mCellConnectionStatus\", \"mCi\", \"mPci\", \"mEarfcn\", "
                           "\"mBandwidth\", \"mMcc\", \"mMnc\", rssi, rsrp, rsrq, rssnr, cqi, \"timingInAdvanced\") "
                           "VALUES (%(deviceID)s, %(operatorID)s,%(batchUUID)s,to_timestamp(%(recordTimeStamp)s/1000.0),%(azimuth)s,%(pitch)s,%(roll)s, %(longitude)s, %(latitude)s, %(altitude)s, %(mRegistered)s, "
                           "%(mTimeStamp)s, %(mCellConnectionStatus)s, %(mCi)s, %(mPci)s, %(mEarfcn)s, "
                           "%(mBandwidth)s, %(mMcc)s, %(mMnc)s, %(rssi)s, %(rsrp)s, %(rsrq)s, %(rssnr)s, %(cqi)s, "
                           "%(timingInAdvanced)s)", item)


        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'Data stored successfully'})

    except jsonschema.exceptions.ValidationError as e:
        print(e)
        return jsonify({'error': 'JSON validation failed.', 'message': e.message}), 400
    except psycopg2.Error as e:
        return jsonify({'error': 'DB Error', 'message':e.message}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
