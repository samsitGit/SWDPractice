import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import csv

class WorkoutApp:
    def __init__(self, master, workout_data):
        self.master = master
        self.workout_data = workout_data
        self.current_index = 0
        self.reps = 0
        self.start_time = time.time()
        self.interrupted = False
        self.timer_id = None
        self.ready_time = 3  # Change the initial countdown time here

        self.label = tk.Label(master, text="Ready for Arm circles (mobility)?", font=("Helvetica", 24), justify="center", pady=20)
        self.label.pack(expand=True, fill="both")
        self.label.bind("<Button-1>", self.start_timer)

    def start_timer(self, event):
        self.label.unbind("<Button-1>")
        self.countdown(self.ready_time)

    def countdown(self, remaining):
        if remaining == 0:
            self.start_exercise()
        else:
            self.label["text"] = str(remaining)
            self.master.after(1000, self.countdown, remaining - 1)

    def start_exercise(self):
        self.interrupted = False
        exercise, exercise_type, duration = self.workout_data[self.current_index]
        self.label["text"] = f"{exercise} ({exercise_type}) - {self.format_duration(duration)}"

        if exercise_type == "mobility":
            self.timer_id = self.master.after(1000, self.update_timer, int(duration), exercise)
            self.label.bind("<Button-1>", self.interrupt_timer)
        else:
            self.label.bind("<Button-1>", self.interrupt_timer)

    def update_timer(self, remaining, exercise):
        if remaining == 0 or self.interrupted:
            self.finish_exercise(exercise)
        else:
            exercise, exercise_type, _ = self.workout_data[self.current_index]
            self.label["text"] = f"{exercise} ({exercise_type}) - {self.format_duration(remaining)}"
            self.timer_id = self.master.after(1000, self.update_timer, remaining - 1, exercise)

    def interrupt_timer(self, event):
        self.interrupted = True
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
            exercise, exercise_type, _ = self.workout_data[self.current_index]
            self.label["text"] = f"{exercise} ({exercise_type}) - Interrupted"
        self.finish_exercise(self.workout_data[self.current_index][0])

    def finish_exercise(self, exercise):
        if not self.interrupted:
            self.reps = int(simpledialog.askstring("Reps", f"Enter the number of reps for {exercise}:"))
        self.current_index += 1

        if self.current_index < len(self.workout_data):
            next_exercise = self.workout_data[self.current_index]  # Get the next exercise data
            next_exercise_name = next_exercise[0]  # Assuming 'Exercise Name' is the key for exercise names
            next_exercise_type = next_exercise[1]
            self.label["text"] = f"Ready for {next_exercise_name} ({next_exercise_type})?"
            self.label.bind("<Button-1>", self.start_timer)
            self.start_time = time.time()  # Update start time for the next exercise
        else:
            self.end_workout()

    def end_workout(self):
        end_time = time.time()
        total_time = round(end_time - self.start_time, 2)

        main_exercises = [exercise for exercise, _, _ in self.workout_data if "(" in exercise]
        misc_exercises = [exercise for exercise, _, _ in self.workout_data if "(" not in exercise]

        main_exercises_time = {exercise: round(sum(d for _, _, d in self.workout_data if exercise in _ and "(" in _), 2) for exercise in main_exercises}
        misc_exercises_time = {exercise: round(sum(d for _, _, d in self.workout_data if exercise in _ and "(" not in _), 2) for exercise in misc_exercises}

        total_time += self.ready_time  # Include the ready time in the total time

        messagebox.showinfo(
            "Workout Completed",
            f"Total time: {total_time}s\n\nMain Exercises:\n{main_exercises_time}\n\nMisc Exercises:\n{misc_exercises_time}"
        )
        self.master.destroy()

    def format_duration(self, duration):
        if isinstance(duration, int):
            return f"{duration}s"
        return f"{duration}s"

def load_exercise_data(program):
    file_path = f"data/{program}.csv"
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        exercises = list(reader)
    return exercises

if __name__ == "__main__":
    start_time = time.time()
    
    workout_data= load_exercise_data("Monday")

    root = tk.Tk()
    root.title("Workout Timer")
    root.geometry("500x200")

    app = WorkoutApp(root, workout_data)
    root.mainloop()
    end_time = time.time()

    total_time = round(end_time - start_time, 2)
    print(total_time)
