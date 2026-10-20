import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

books = [
    {"id": "A-04", "title": "1984", "author": "George Orwell", "category": "Fiction", "year": 1949, "available": "0 of 4 available", "status": "Out", "color": "bg-red-800"},
    {"id": "B-12", "title": "A Brief History of Time", "author": "Stephen Hawking", "category": "Science", "year": 1988, "available": "2 of 3 available", "status": "Available", "color": "bg-blue-600"},
    {"id": "D-01", "title": "Clean Code", "author": "Robert C. Martin", "category": "Technology", "year": 2008, "available": "4 of 6 available", "status": "Available", "color": "bg-emerald-600"},
    {"id": "B-01", "title": "Cosmos", "author": "Carl Sagan", "category": "Science", "year": 1980, "available": "3 of 4 available", "status": "Available", "color": "bg-indigo-700"},
    {"id": "D-02", "title": "Design Patterns", "author": "Erich Gamma", "category": "Technology", "year": 1994, "available": "3 of 3 available", "status": "Available", "color": "bg-indigo-900"},
    {"id": "C-04", "title": "Guns, Germs, and Steel", "author": "Jared Diamond", "category": "History", "year": 1997, "available": "1 of 2 available", "status": "Available", "color": "bg-amber-900"},
    {"id": "D-03", "title": "Introduction to Algorithms", "author": "Thomas Cormen", "category": "Technology", "year": 2009, "available": "2 of 4 available", "status": "Available", "color": "bg-teal-800"},
    {"id": "A-03", "title": "Pride and Prejudice", "author": "Jane Austen", "category": "Fiction", "year": 1813, "available": "3 of 3 available", "status": "Available", "color": "bg-pink-900"},
]

members = [
    {"name": "Aarav Sharma", "email": "aarav.sharma@lumina.edu", "type": "Student", "dept": "Computer Science", "contact": "+91 98765 43210", "joined": "Jan 15, 2025", "status": "Active"},
    {"name": "Ananya Iyer", "email": "ananya.iyer@lumina.edu", "type": "Student", "dept": "Computer Science", "contact": "+91 98765 43213", "joined": "Feb 10, 2025", "status": "Active"},
    {"name": "Arjun Mehta", "email": "arjun.mehta@lumina.edu", "type": "Staff", "dept": "Administration", "contact": "+91 98765 43219", "joined": "Jul 10, 2024", "status": "Active"},
    {"name": "Diya Patel", "email": "diya.patel@lumina.edu", "type": "Student", "dept": "Electronics", "contact": "+91 98765 43211", "joined": "Jan 20, 2025", "status": "Active"},
    {"name": "Sakshi", "email": "sakshi@lumina.edu", "type": "Faculty", "dept": "Library Science", "contact": "+91 98765 43217", "joined": "Jun 1, 2024", "status": "Active"}
]

circulation = [
    {"book": "A Brief History of...", "member": "Kabir Singh", "issue": "Oct 8, 2025", "due": "Oct 22, 2025", "return": "--", "status": "Issued"},
    {"book": "Sapiens", "member": "Ananya Iyer", "issue": "Oct 5, 2025", "due": "Oct 19, 2025", "return": "--", "status": "Overdue"}
]

@app.route('/')
def home():
    return render_template('index.html', books=books, members=members, circulation=circulation)

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/api/members', methods=['GET'])
def get_members():
    return jsonify(members)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)