import tkinter as tk 


class StudyPlannerApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Study Planner")
        self.root.geometry("760x520")

    def run(self) -> None:
        self.root.mainloop()