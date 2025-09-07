from flask import Flask, request, render_template_string

app = Flask(__name__)

#  book dataset (book: genre)
books = {
    "Sapiens: A Brief History of Humankind": "History Non-Fiction",
    "The Midnight Library": "Fiction Novel",
    "Deep Work": "Productivity Non-Fiction",
    "The Silent Patient": "Thriller Fiction",
    "Atomic Habits": "Self-help Productivity",
    "Homo Deus": "History Non-Fiction",
    "The Alchemist": "Fiction Novel",
    "Norwegian Wood": "Fiction Romance",
}

#  Recommendation function
def recommend(book_name):
    book_name = book_name.lower().strip()

    matched_book = None
    for title in books.keys():
        if book_name in title.lower():
            matched_book = title
            break

    # If book not found → return default list
    if not matched_book:
        return ["Sapiens: A Brief History of Humankind",
                "The Midnight Library",
                "Deep Work"]

    target_genre = books[matched_book].split()[0]

    recommendations = []
    for book, genre in books.items():
        if book != matched_book and target_genre in genre:
            recommendations.append(book)

    return recommendations if recommendations else [
        "The Alchemist",
        "Norwegian Wood"
    ]

# 🖥 HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Book Recommendation System</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f8ff; text-align: center; }
        .container { margin-top: 50px; }
        input[type=text] { padding: 10px; width: 300px; }
        input[type=submit] { padding: 10px; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 8px 0; }
        a { text-decoration: none; color: darkblue; font-weight: bold; }
        a:hover { color: green; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Book Recommendation System</h1>
        <form method="POST">
            <input type="text" name="book" placeholder="Enter book name" required>
            <input type="submit" value="Search">
        </form>

        {% if user_input %}
            <h2>You searched for: "{{ user_input }}"</h2>
            <h3>Recommended Books:</h3>
            <ul>
                {% for book in recommendations %}
                    <li><a href="/?book={{ book }}">{{ book }}</a></li>
                {% endfor %}
            </ul>
        {% endif %}
    </div>
</body>
</html>
"""

#  Flask routes
@app.route("/", methods=["GET", "POST"])
def home():
    user_input = None
    recommendations = []

    if request.method == "POST":
        user_input = request.form.get("book")
        recommendations = recommend(user_input)

    # Handle GET request if user clicks a recommendation
    elif request.method == "GET" and "book" in request.args:
        user_input = request.args.get("book")
        recommendations = recommend(user_input)

    return render_template_string(HTML_TEMPLATE, user_input=user_input, recommendations=recommendations)


if __name__ == "__main__":
    app.run(debug=True)
