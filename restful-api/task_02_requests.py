#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:  # Fixed: was 'for posts in posts' (variable shadowing)
            print(post['title'])

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")  # Fixed: typo 'reponse'
    if response.status_code == 200:
        posts = response.json()  # Fixed: renamed 'post' to 'posts' for clarity
        data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=['id', 'title', 'body']
            )
            writer.writeheader()
            writer.writerows(data)