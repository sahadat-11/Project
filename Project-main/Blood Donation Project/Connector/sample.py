from flask import Flask, jsonify, request

app = Flask(__name__)

# Division, District, Upazila data
data = {
    "BARISHAL": {
        "BARGUNA": ["AMTALI", "BAMNA", "BARGUNA SADAR", "BETAGI", "PATHARGHATA", "TALTALI"],
        "BARISAL": ["AGAILJHARA", "BABUGANJ", "BAKERGANJ", "BANARI PARA", "GAURNADI", "HIZLA", "BARISAL SADAR", "MHENDIGANJ", "MULADI", "WAZIRPUR"],
        # ... Other districts
    },
    "CHATTOGRAM": {
        "BANDARBAN": ["ALIKADAM", "BANDARBAN SADAR", "LAMA", "NAIKHONGCHHARI", "ROWANGCHHARI", "RUMA", "THANCHI"],
        # ... Other districts
    },
    # ... Other divisions
}

@app.route('/divisions', methods=['GET'])
def get_divisions():
    return jsonify(list(data.keys()))

@app.route('/districts/<division>', methods=['GET'])
def get_districts(division):
    division_data = data.get(division.upper())
    if not division_data:
        return jsonify({"error": "Division not found"}), 404
    return jsonify(list(division_data.keys()))

@app.route('/upazilas/<division>/<district>', methods=['GET'])
def get_upazilas(division, district):
    division_data = data.get(division.upper())
    if not division_data:
        return jsonify({"error": "Division not found"}), 404
    district_data = division_data.get(district.upper())
    if not district_data:
        return jsonify({"error": "District not found"}), 404
    return jsonify(district_data)

if __name__ == '__main__':
    app.run(debug=True)
