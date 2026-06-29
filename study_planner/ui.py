import tkinter as tk 
from .storage import JsonTaskRepository
from .config import FILTERS, PRIORITIES, TASKS_FILE
from tkinter import messagebox, ttk


class StudyPlannerApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Study Planner")
        self.root.geometry("760x520")
        self.root.minsize(640, 440)

        repository = JsonTaskRepository(TASKS_FILE)

        self.title_var= tk.StringVar()
        self.deadline_var = tk.StringVar()
        self.priority_var = tk.StringVar(value=PRIORITIES[1])
        self.filter_var = tk.StringVar(value=FILTERS[0])
        self.stats_var = tk.StringVar()

        self._build_ui()

    def run(self) -> None:
        self.root.mainloop()


    def _build_ui(self) -> None:
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        form = ttk.LabelFrame(self.root, text="Новая задача", padding=12)
        form.grid(row=0, column=0, padx=12, pady=(12, 6), sticky="ew")
        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="Название:").grid(row=0, column=0, padx=(0,8), pady=4, sticky="w")
        ttk.Entry(form, textvariable=self.title_var).grid(row=0, column=1, padx=(0,8), pady=4, sticky="ew")

        ttk.Label(form, text="Дедлайн:").grid(row=1, column=0, padx=(0,8), pady=4, sticky="w")
        ttk.Entry(form, textvariable=self.deadline_var).grid(row=1, column=1, padx=(0,8), pady=4, sticky="ew")
        ttk.Label(form, text="ДД.ММ.ГГГГ").grid(row=1, column=2, pady=4, sticky="w")


        ttk.Label(form, text="Приоритет: ").grid(row=2, column=0, padx=(0,8), pady=4, sticky="w")
        ttk.Combobox(
            form,
            textvariable=self.priority_var,
            values=PRIORITIES,
            state="readonly",
            width=18
        ).grid(row=2, column=1, padx=(0,8), pady=4, sticky="w")

        buttons = ttk.Frame(form)
        buttons.grid(row=3, column=1, pady=(8,0), sticky="w")
        ttk.Button(buttons, text="Добавить задачу", command=...).grid(row=0, column=0, padx=(0,8))
        ttk.Button(buttons, text="Очистить", command=self._clear_form).grid(row=0, column=1)


    def _clear_form(self) -> None:
        self.title_var.set("")
        self.deadline_var.set("")
        self.priority_var.set(PRIORITIES[1])