from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['todo_db']
collection = db['todo_items']

@app.route('/')
def form():
    return render_template('form.html')


# ✅ REQUIRED ROUTE (Assignment)
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    try:
        itemName = request.form.get('itemName')
        itemDescription = request.form.get('itemDescription')

        # Optional fields (for later step)
        itemId = request.form.get('itemId')
        itemUUID = request.form.get('itemUUID')
        itemHash = request.form.get('itemHash')

        collection.insert_one({
            'itemName': itemName,
            'itemDescription': itemDescription,
            'itemId': itemId,
            'itemUUID': itemUUID,
            'itemHash': itemHash
        })

        return render_template('form.html', success="To-Do Item Added Successfully")

    except Exception as e:
        print(f"Error: {e}")
        return render_template('form.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)