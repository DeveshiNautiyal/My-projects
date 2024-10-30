import tkinter as tk
from tkinter import messagebox, scrolledtext 

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
  
    def __str__(self):
        return"{self.title} by {self.author}"

class User:
    def __init__(self, name, preference=None):
        self.name = name
        self.preferences = preference if preference else []

    def add_preference(self, genre):
        if genre not in self.preference:
            self.preference.append(genre)

    def get_recommendations(self, books):
        recommended_books = []
        for book in books:
            if book.genre in self.preferences:
                recommended_books.append(book)
        return recommended_books

class BookRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Recommendation System")

        self.label_name = tk.Label(self.root, text="Name,Please:")
        self.label_name.pack()

        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack()

        self.label_preferences = tk.Label(self.root, text="Preferred genres:")
        self.label_preferences.pack()

        self.entry_preferences = tk.Entry(self.root)
        self.entry_preferences.pack()

        self.submit_button = tk.Button(self.root, text=" Preferences", command=self.submit_preferences, bg="green", fg="white")
        self.submit_button.pack(pady=10)

        self.recommend_button = tk.Button(self.root, text=" Recommendations", command=self.get_recommendations, bg="blue", fg="white")
        self.recommend_button.pack(pady=10)
        
       
    def submit_preferences(self):
        preferences_input = self.entry_preferences.get().strip()
        if preferences_input:
            preferences = [genre.strip() for genre in preferences_input.split(',') if genre.strip()]
            for genre in preferences:
                self.entry_preferences.delete(0, tk.END)
                self.entry_preferences.insert(tk.END, genre)

    def get_recommendations(self):
        name = self.entry_name.get().strip()
        preferences = [genre.strip() for genre in self.entry_preferences.get().split(',') if genre.strip()]

        if not name or not preferences:
            messagebox.showerror("Error", "Please enter your name and genres of the book.")
            return

        user = User(name, preferences)
        recommended_books = user.get_recommendations(books)

        if recommended_books:
            self.display_recommendations(recommended_books, name)
        else:
            messagebox.showinfo("Recommendations", f"Heyyy {name}, sorry,unfortunately we don't have recommendations for your preferences.")

    def display_recommendations(self, recommended_books, username):
        #another window 
        recommendation_window = tk.Toplevel(self.root)
        recommendation_window.title("Recommended Books")
        recommendation_window.configure(bg="lightblue")

        #scroll text widget   
        text_area = scrolledtext.ScrolledText(recommendation_window, width=50, height=20, wrap=tk.WORD)
        text_area.pack(padx=30, pady=10)

        # Format and insert recommended books into the text area
        text_area.tag_configure("bold", font=("lucida calligraphy", 10, "bold"))
        text_area.tag_configure("italic", font=("Lucida calligraphy", 10, "italic"))
        
        text_area.insert(tk.END, f"Heyyy {username}, here are your recommended books:\n\n")
        for book in recommended_books:
            text_area.insert(tk.END, f"{book.title} by {book.author}\n", "bold")
            text_area.insert(tk.END, f"Genre: {book.genre}\n\n", "italic")

        # Disable editing in the text area
        text_area.configure(state=tk.DISABLED)

if __name__ == "__main__":
    # Creating books
    books = [
        Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
        Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"),
        Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "Non-fiction"),
        Book("The Martian", "Andy Weir", "Science Fiction"),
        Book("1984", "George Orwell", "Dystopian"),
        Book("Becoming", "Michelle Obama", "Memoir"),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
        Book("Pride and Prejudice", "Jane Austen", "Classic"),
        Book("The Hunger Games", "Suzanne Collins", "Young Adult"),
        Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy"),
        Book("The Da Vinci Code", "Dan Brown", "Mystery"),
        Book("Gone with the Wind", "Margaret Mitchell", "Historical Fiction"),
        Book("The Alchemist", "Paulo Coelho", "Philosophical Fiction"),
        Book("The Road", "Cormac McCarthy", "Post-Apocalyptic"),
        Book("The Girl with the Dragon Tattoo", "Stieg Larsson", "Crime"),
        Book("The Shining", "Stephen King", "Horror"),
        Book("The Help", "Kathryn Stockett", "Drama"),
        Book("The Handmaid's Tale", "Margaret Atwood", "Dystopian"),
        Book("Moby-Dick", "Herman Melville", "Adventure"),
        Book("The Goldfinch", "Donna Tartt", "Literary Fiction"),
        Book("The Sun Also Rises", "Ernest Hemingway", "Modernist"),
        Book("The Odyssey", "Homer", "Epic"),
        Book("One Hundred Years of Solitude", "Gabriel García Márquez", "Magical Realism"),
        Book("The Picture of Dorian Gray", "Oscar Wilde", "Gothic"),
        Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction"),
        Book("The Night Circus", "Erin Morgenstern", "Fantasy"),
        Book("The Kite Runner", "Khaled Hosseini", "Contemporary"),
        Book("The Count of Monte Cristo", "Alexandre Dumas", "Adventure"),
        Book("Jane Eyre", "Charlotte Brontë", "Gothic"),
        Book("Little Women", "Louisa May Alcott", "Children's"),
        Book("Wuthering Heights", "Emily Brontë", "Gothic"),
        Book("Brave New World", "Aldous Huxley", "Dystopian"),
        Book("The Catch-22", "Joseph Heller", "Satire"),
        Book("Frankenstein", "Mary Shelley", "Gothic"),
        Book("The Bell Jar", "Sylvia Plath", "Autobiographical"),
        Book("The Color Purple", "Alice Walker", "Epistolary"),
        Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy"),
        Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"),
        Book("Invisible Man", "Ralph Ellison", "Modernist"),
        Book("Life of Pi", "Yann Martel", "Adventure"),
        Book("The Grapes of Wrath", "John Steinbeck", "Realist"),
        Book("The Road Less Traveled", "M. Scott Peck", "Self-help"),
        Book("Crime and Punishment", "Fyodor Dostoevsky", "Psychological Fiction"),
        Book("Anna Karenina", "Leo Tolstoy", "Realist"),
        Book("Beloved", "Toni Morrison", "Magical Realism"),
        Book("Middlemarch", "George Eliot", "Realist"),
        Book("East of Eden", "John Steinbeck", "Realist"),
        Book("The Stand", "Stephen King", "Post-Apocalyptic"),
        Book("The Brothers Karamazov", "Fyodor Dostoevsky", "Philosophical Fiction"),
        Book("The Road to Wigan Pier", "George Orwell", "Social Criticism"),
        Book("The Wind-Up Bird Chronicle", "Haruki Murakami", "Magical Realism"),
        Book("A Game of Thrones", "George R.R. Martin", "Fantasy"),
        Book("The Shadow of the Wind", "Carlos Ruiz Zafón", "Gothic"),
        Book("The Name of the Wind", "Patrick Rothfuss", "Fantasy"),
        Book("The Handmaid's Tale", "Margaret Atwood", "Dystopian"),
        Book("The Metamorphosis", "Franz Kafka", "Absurdist Fiction"),
        Book("Nineteen Eighty-Four", "George Orwell", "Dystopian"),
        Book("The Secret History", "Donna Tartt", "Mystery"),
        Book("The Girl on the Train", "Paula Hawkins", "Thriller"),
        Book("The Book Thief", "Markus Zusak", "Historical Fiction"),
        Book("Educated", "Tara Westover", "Memoir"),
        Book("American Gods", "Neil Gaiman", "Fantasy"),
        Book("Where the Crawdads Sing", "Delia Owens", "Mystery"),
        Book("Crazy Rich Asians", "Kevin Kwan", "Contemporary"),
        Book("The Nightingale", "Kristin Hannah", "Historical Fiction"),
        Book("The Underground Railroad", "Colson Whitehead", "Historical Fiction"),
        Book("A Man Called Ove", "Fredrik Backman", "Humor"),
        Book("The Martian", "Andy Weir", "Science Fiction"),
        Book("The Help", "Kathryn Stockett", "Drama"),
        Book("The Giver", "Lois Lowry", "Young Adult"),
        Book("The Immortalists", "Chloe Benjamin", "Fantasy"),
        Book("A Little Life", "Hanya Yanagihara", "Literary Fiction"),
        Book("All the Light We Cannot See", "Anthony Doerr", "Historical Fiction"),
        Book("Sharp Objects", "Gillian Flynn", "Mystery"),
        Book("The Goldfinch", "Donna Tartt", "Literary Fiction"),
        Book("The Handmaid's Tale", "Margaret Atwood", "Dystopian"),
        Book("The Testaments", "Margaret Atwood", "Dystopian"),
        Book("The Ocean at the End of the Lane", "Neil Gaiman", "Fantasy"),
        Book("The Night Circus", "Erin Morgenstern", "Fantasy"),
        Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
        Book("Pride and Prejudice", "Jane Austen", "Fiction"),
        Book("One Hundred Years of Solitude", "Gabriel García Márquez", "Fiction"),
        Book("The Alchemist", "Paulo Coelho", "Fiction"),
        Book("The Road", "Cormac McCarthy", "Fiction"),
        Book("Life of Pi", "Yann Martel", "Fiction"),
        Book("Beloved", "Toni Morrison", "Fiction"),
        Book("The Handmaid's Tale", "Margaret Atwood", "Fiction"),
    ]

    # Create GUI window
    root = tk.Tk()
    root.configure(bg="lightgreen")
    
    app = BookRecommendationApp(root)

    # Customize button colors
    app.submit_button.configure(bg="green", fg="white")
    app.recommend_button.configure(bg="blue", fg="white")
    
    
    root.mainloop()

