import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('snake_game.db')
        self.cursor = self.conn.cursor()
    
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TIMESTAMP NOT NULL
            )
        ''')
        self.conn.commit()
    
    def save_score(self, player_name, score):
        self.cursor.execute('''
            INSERT INTO scores (player_name, score, date)
            VALUES (?, ?, ?)
        ''', (player_name, score, datetime.now()))
        self.conn.commit()
    
    def get_high_scores(self, limit=10):
        self.cursor.execute('''
            SELECT player_name, score, date
            FROM scores
            ORDER BY score DESC
            LIMIT ?
        ''', (limit,))
        return self.cursor.fetchall()
    
    def __del__(self):
        self.conn.close() 