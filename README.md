# Mahasiswa Classifier 

First time trying Object-Oriented Programming. This is a simple command-line Python project to input, store, and evaluate student data (`mahasiswa`)

I build this right after finishing [freeCodeCamp’s 4-hour Python course](https://www.youtube.com/watch?v=rfscVS0vtbw) with minimal guidance. Tbh i think i spent too much time and effort on this

Update : Added a persistent data storing with JSON

## 🔍 What does it do?
- Input data for multiple students
- Built using classes and object instances
- Add new student data via terminal
- Store data persistently in mhs.json
- Simple read/filter operations:
  - View all students
  - View high achievers (IPK>=3.5)
- Delete data based on:
  - Name
  - Age
  - Faculty
- Undo last deletion via backup file
- Input validation with loops and error catching

## 📁 File Structure
gig1/
├── mahasiswa.py         # Mahasiswa class with to_dict() method
├── main.py              # Your main script
├── mhs.json             # Main data file
├── backup.json          # Used for undoing deletions

## 📚 What I Learned
- Object-Oriented Programming (Classes, Instances)
- File I/O with JSON
- Input validation & loops
- Data filtering using list comprehensions
- Project structuring and Git/GitHub basics



