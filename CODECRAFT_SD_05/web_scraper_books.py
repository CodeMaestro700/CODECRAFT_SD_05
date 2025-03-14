import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import messagebox

def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.select('.product_pod')

    product_list = []

    for book in books:
        title = book.h3.a['title']
        price = book.select_one('.price_color').text
        rating_class = book.select_one('p.star-rating')['class']
        rating = rating_class[1]  # 'One', 'Two', etc.

        product_list.append([title, price, rating])

    with open("products.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Rating"])
        writer.writerows(product_list)

    messagebox.showinfo("Done!", f"Scraped {len(product_list)} products into 'products.csv'")

# Create GUI
root = tk.Tk()
root.title("Book Scraper")
root.geometry("300x150")

label = tk.Label(root, text="Click to scrape books!", font=("Arial", 12))
label.pack(pady=20)

scrape_button = tk.Button(root, text="Scrape Books", command=scrape_books, font=("Arial", 12), bg="lightblue")
scrape_button.pack(pady=10)

root.mainloop()
