import sys
from flask import jsonify
from flask import Flask
from flask_restful import Api
from flask_restful import reqparse
from flask_restful import Resource


app = Flask(__name__)
api = Api(app)

string_cols = ['job', 'marital', 'education', 'default', 'housing',
               'loan', 'contact', 'month', 'day_of_week', 'poutcome',
               'sample_uuid']

int_cols = ['age', 'duration', 'campaign', 'pdays', 'previous']

float_cols = ['emp.var.rate', 'cons.wprice.idx', 'cons.conf.idx',
              'euribor3m', 'nr.employed', 'label']

parser = reqparse.RequestParser()
for col in string_cols:
    parser.add_argument(col, type=str)

for col in float_cols:
    parser.add_argument(col, type=float)

for col in int_cols:
    parser.add_argument(col, type=int)


class Predict(Resource):

    def get(self):
        arguments = parser.parse_args()
        result = {
            'probability': 0.5,
            'label': 1.,
            'sample_uuid': arguments['sample_uuid'],
        }
        return jsonify(**result)


api.add_resource(Predict, '/api/v1/predict')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        host = None
        port = None

    app.run(host=host, port=port, debug=False)
