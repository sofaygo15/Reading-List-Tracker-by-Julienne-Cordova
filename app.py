from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample book list (in-memory storage)
reading_list = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "status": "read"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "to-read"},
    {"title": "Moby Dick", "author": "Herman Melville", "genre": "Adventure", "status": "read"}
]

@app.route('/')
def index():
    filter_status = request.args.get('status')
    if filter_status:
        filtered_books = [book for book in reading_list if book['status'] == filter_status]
    else:
        filtered_books = reading_list
    return render_template('index.html', books=filtered_books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        status = request.form['status']
        reading_list.append({"title": title, "author": author, "genre": genre, "status": status})
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/update/<int:book_index>', methods=['GET', 'POST'])
def update_book(book_index):
    book = reading_list[book_index]
    if request.method == 'POST':
        book['status'] = request.form['status']
        return redirect(url_for('index'))
    return render_template('update_book.html', book=book, index=book_index)

@app.route('/remove/<int:book_index>')
def remove_book(book_index):
    reading_list.pop(book_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
