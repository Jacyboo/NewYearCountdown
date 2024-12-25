import customtkinter as ctk
from datetime import datetime
import time

class CountdownApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("New Year Countdown")
        self.window.geometry("700x400")
        self.window.configure(fg_color="#000000")
        
        # Set the appearance mode to dark
        ctk.set_appearance_mode("dark")
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        self.main_frame.pack(expand=True, fill="both", padx=40, pady=30)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="NEW YEAR COUNTDOWN",
            font=("Helvetica", 32, "bold"),
            text_color="#ffffff"
        )
        self.title_label.pack(pady=(0, 30))
        
        # Time labels
        self.time_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.time_frame.pack(expand=True)
        
        # Create time unit displays
        self.units = ['Weeks', 'Days', 'Hours', 'Minutes', 'Seconds']
        self.time_labels = {}
        
        for i, unit in enumerate(self.units):
            frame = ctk.CTkFrame(self.time_frame, fg_color="#111111", corner_radius=15)
            frame.grid(row=0, column=i, padx=15, pady=10)
            
            self.time_labels[unit] = ctk.CTkLabel(
                frame,
                text="00",
                font=("Helvetica", 42, "bold"),
                text_color="#ffffff"
            )
            self.time_labels[unit].pack(padx=25, pady=(15, 5))
            
            ctk.CTkLabel(
                frame,
                text=unit.upper(),
                font=("Helvetica", 12),
                text_color="#666666"
            ).pack(pady=(0, 15))
        
        self.update_time()
        
    def calculate_time_until_new_year(self):
        now = datetime.now()
        next_year = datetime(now.year + 1, 1, 1)
        diff = next_year - now
        
        # Calculate all time units
        total_seconds = diff.total_seconds()
        seconds = int(total_seconds % 60)
        minutes = int((total_seconds // 60) % 60)
        hours = int((total_seconds // 3600) % 24)
        total_days = diff.days
        weeks = total_days // 7
        days = total_days % 7
        
        return {
            'Weeks': weeks,
            'Days': days,
            'Hours': hours,
            'Minutes': minutes,
            'Seconds': seconds
        }
    
    def update_time(self):
        time_left = self.calculate_time_until_new_year()
        
        for unit, value in time_left.items():
            self.time_labels[unit].configure(text=f"{value:02d}")
        
        self.window.after(1000, self.update_time)  # Update every second
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = CountdownApp()
    app.run() 