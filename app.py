from flask import Flask, request, jsonify, render_template
from scraper import extract_reviews

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    url = request.args.get('page')
    if not url:
        return jsonify({"error": "URL parameter 'page' is required."}), 400

    try:
        reviews_data = extract_reviews(url, max_pages=10)  # Set maximum pages to 10
        return jsonify(reviews_data)
    except Exception as e:
        import traceback
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500


if __name__ == '__main__':
    app.run(debug=True)
