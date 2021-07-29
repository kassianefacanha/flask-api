from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

dados = [{
    'name': 'Dados',
    'items': [{'name':'my item',
                'resolution': 'string',
                'issue_summary_id': 0,
                'family_id': 0,
                'system_id': 0,
                'region_code': 0 }]
}]

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/resolution_template' , methods=['POST'])
def create_resolution_template():
  request_data = request.get_json()
  new_dados = {
    'items':[]
  }
  dados.append(new_dados)
  return jsonify(new_dados)

@app.route('/resolution_template/<string:name>')
def get_resolution_template(name):
  for resolution_template in dados:
    if resolution_template['name'] == name:
          return jsonify(resolution_template)
  return jsonify ({'message': 'resolution_template not found'})
 
@app.route('/resolution_template')
def get_dados():
  return jsonify({'dados': dados})
 
@app.route('/resolution_template/<string:name>/item' , methods=['POST'])
def create_item_in_resolution_template(name):
  request_data = request.get_json()
  for resolution_template in dados:
    if resolution_template['name'] == name:
        new_item = {
            'name': request_data['name'],
            'resolution': request_data['resolution'],
            'issue_summary_id': request_data['issue_summary_id'],
            'family_id': request_data['family_id'],
            'system_id': request_data['system_id'],
            'region_code': request_data['region_code'],
        }
        resolution_template['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'resolution_template not found'})


@app.route('/resolution_template/<string:name>/item')
def get_item_in_resolution_template(name):
  for resolution_template in dados:
    if resolution_template['name'] == name:
        return jsonify( {'items':resolution_template['items'] } )
  return jsonify ({'message':'resolution_template not found'})

  
app.run(port=5000)