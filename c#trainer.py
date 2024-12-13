import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import tempfile
import os
import json
import textwrap

# ---------------------------
# Module Content Definitions
# ---------------------------

introduction_content = {
    "title": "Introduction to C#",
    "sections": [
        {
            "heading": "What is C#?",
            "content": textwrap.dedent("""
                C# is a modern, object-oriented programming language developed by Microsoft and standardized by ECMA and ISO. 
                It is designed for building a wide range of applications that run on the .NET framework.

                **Key Features:**
                - **Object-Oriented:** Supports encapsulation, inheritance, and polymorphism.
                - **Type-Safe:** Prevents type errors during compilation.
                - **Modern Constructs:** Includes LINQ, async/await, and more.
                - **Rich Standard Library:** Extensive libraries for various functionalities.
                - **Cross-Platform:** Develop applications for Windows, Linux, macOS, and more.
            """)
        },
        {
            "heading": "Hello, World!",
            "content": textwrap.dedent("""
                The classic first program prints "Hello, World!" to the console.

                ```csharp
                using System;

                namespace HelloWorld
                {
                    class Program
                    {
                        static void Main(string[] args)
                        {
                            Console.WriteLine("Hello, World!");
                        }
                    }
                }
                ```
            """)
        }
    ]
}

basics_content = {
    "title": "C# Basics",
    "sections": [
        {
            "heading": "Data Types & Variables",
            "content": textwrap.dedent("""
                C# is statically typed, meaning each variable and object has a known type at compile time.

                **Common Data Types:**
                - `int`: For integers
                - `double`: For floating-point numbers
                - `bool`: For boolean values (`true`/`false`)
                - `string`: For text
                - `char`: For a single character

                **Example:**

                ```csharp
                int number = 10;
                double pi = 3.14159;
                bool isActive = true;
                string greeting = "Hello, C#!";
                char letter = 'A';
                ```
            """)
        },
        {
            "heading": "Control Structures",
            "content": textwrap.dedent("""
                C# provides familiar control flow statements like `if`, `for`, `while`, and `foreach`.

                **If Statement:**

                ```csharp
                if (number > 0)
                {
                    Console.WriteLine("Positive number");
                }
                else
                {
                    Console.WriteLine("Zero or negative number");
                }
                ```

                **For Loop:**

                ```csharp
                for (int i = 0; i < 5; i++)
                {
                    Console.WriteLine("Iteration: " + i);
                }
                ```

                **Foreach Loop:**

                ```csharp
                string[] fruits = { "Apple", "Banana", "Cherry" };
                foreach (var fruit in fruits)
                {
                    Console.WriteLine(fruit);
                }
                ```
            """)
        },
        {
            "heading": "Methods",
            "content": textwrap.dedent("""
                Methods in C# define reusable blocks of code.

                ```csharp
                public int Add(int a, int b)
                {
                    return a + b;
                }
                ```

                Methods can also be asynchronous using `async`/`await` keywords or defined as `static` if they belong to the class rather than an instance.
            """)
        }
    ]
}

advanced_content = {
    "title": "Advanced C# Topics",
    "sections": [
        {
            "heading": "Asynchronous Programming with async/await",
            "content": textwrap.dedent("""
                Asynchronous programming helps keep applications responsive. With `async` and `await`:

                ```csharp
                public async Task FetchDataAsync()
                {
                    using HttpClient client = new HttpClient();
                    string data = await client.GetStringAsync("https://api.example.com/data");
                    Console.WriteLine(data);
                }
                ```

                This allows the application to continue running while waiting for I/O operations to complete.
            """)
        },
        {
            "heading": "LINQ (Language Integrated Query)",
            "content": textwrap.dedent("""
                LINQ provides a declarative syntax for querying in-memory collections.

                **Example: Filtering a List:**

                ```csharp
                List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
                var evenNumbers = numbers.Where(n => n % 2 == 0);

                foreach (int num in evenNumbers)
                {
                    Console.WriteLine(num);
                }
                ```
            """)
        },
        {
            "heading": "Generics",
            "content": textwrap.dedent("""
                Generics let you define type-safe data structures.

                ```csharp
                List<string> names = new List<string>();
                names.Add("Alice");
                names.Add("Bob");
                ```

                With generics, you avoid boxing/unboxing and get compile-time type checks.
            """)
        },
        {
            "heading": "Reflection",
            "content": textwrap.dedent("""
                Reflection allows you to inspect types at runtime.

                ```csharp
                Type typeInfo = typeof(MyClass);
                var methods = typeInfo.GetMethods();

                foreach (var method in methods)
                {
                    Console.WriteLine(method.Name);
                }
                ```
            """)
        },
        {
            "heading": "Delegates and Events",
            "content": textwrap.dedent("""
                Delegates are type-safe function pointers, and events provide a way to notify subscribers.

                **Example:**

                ```csharp
                public delegate void Notify(string message);

                public class Process
                {
                    public event Notify ProcessCompleted;

                    public void StartProcess()
                    {
                        // Process logic here
                        OnProcessCompleted("Process finished successfully.");
                    }

                    protected virtual void OnProcessCompleted(string message)
                    {
                        ProcessCompleted?.Invoke(message);
                    }
                }
                ```
            """)
        },
        {
            "heading": "Interfaces and Abstract Classes",
            "content": textwrap.dedent("""
                Interfaces and abstract classes allow you to define contracts and base implementations.

                **Interface Example:**

                ```csharp
                public interface IAnimal
                {
                    void Speak();
                }

                public class Dog : IAnimal
                {
                    public void Speak()
                    {
                        Console.WriteLine("Woof!");
                    }
                }
                ```

                **Abstract Class Example:**

                ```csharp
                public abstract class Shape
                {
                    public abstract double Area();
                }

                public class Circle : Shape
                {
                    public double Radius { get; set; }

                    public override double Area()
                    {
                        return Math.PI * Radius * Radius;
                    }
                }
                ```
            """)
        },
        {
            "heading": "Dependency Injection",
            "content": textwrap.dedent("""
                Dependency Injection (DI) is a design pattern that allows for decoupling dependencies, making code more modular and testable.

                **Example Using Constructor Injection:**

                ```csharp
                public interface ILogger
                {
                    void Log(string message);
                }

                public class ConsoleLogger : ILogger
                {
                    public void Log(string message)
                    {
                        Console.WriteLine(message);
                    }
                }

                public class UserService
                {
                    private readonly ILogger _logger;

                    public UserService(ILogger logger)
                    {
                        _logger = logger;
                    }

                    public void CreateUser(string username)
                    {
                        // Create user logic
                        _logger.Log($"User {username} created.");
                    }
                }
                ```
            """)
        },
        {
            "heading": "Design Patterns",
            "content": textwrap.dedent("""
                Design Patterns provide reusable solutions to common software design problems.

                **Singleton Pattern Example:**

                ```csharp
                public class Singleton
                {
                    private static Singleton _instance;

                    private Singleton() { }

                    public static Singleton Instance
                    {
                        get
                        {
                            if (_instance == null)
                            {
                                _instance = new Singleton();
                            }
                            return _instance;
                        }
                    }

                    public void DoSomething()
                    {
                        Console.WriteLine("Singleton instance method called.");
                    }
                }
                ```
            """)
        }
    ]
}

quizzes_content = {
    "title": "Quizzes",
    "sections": [
        {
            "heading": "Test Your Knowledge",
            "content": textwrap.dedent("""
                Below are some multiple-choice questions to evaluate what you have learned.
                Select your answers and press "Submit" to see your score.
            """)
        }
    ]
}

glossary_content = {
    "title": "Glossary",
    "sections": [
        {
            "heading": "Key Terms",
            "content": textwrap.dedent("""
                **Encapsulation**: The bundling of data with the methods that operate on that data.

                **Inheritance**: A mechanism where one class acquires the property of another class.

                **Polymorphism**: The ability of different classes to be treated as instances of the same class through inheritance.

                **Delegates**: Type-safe function pointers used to pass methods as arguments.

                **Async/Await**: Keywords used to write asynchronous code more easily.

                **LINQ**: Language Integrated Query, used for querying data in a more readable way.

                **Generics**: Allow classes and methods to operate with any data type without sacrificing type safety.

                **Reflection**: The ability of a program to inspect and modify its own structure and behavior at runtime.

                **Dependency Injection**: A design pattern that implements inversion of control for resolving dependencies.

                **Design Patterns**: Reusable solutions to common software design problems.
            """)
        }
    ]
}

references_content = {
    "title": "References and Resources",
    "sections": [
        {
            "heading": "Further Reading",
            "content": textwrap.dedent("""
                - [Microsoft C# Documentation](https://docs.microsoft.com/en-us/dotnet/csharp/)
                - [C# Programming Guide](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/)
                - [C# Tutorials on Microsoft Learn](https://docs.microsoft.com/en-us/learn/paths/csharp-first-steps/)
                - [Pro C# 8 with .NET Core](https://www.apress.com/gp/book/9781484257552)
                - [C# Design Patterns](https://www.dofactory.com/net/design-patterns)
            """)
        }
    ]
}

modules = {
    "Introduction": introduction_content,
    "Basics": basics_content,
    "Advanced Topics": advanced_content,
    "Quizzes": quizzes_content,
    "Glossary": glossary_content,
    "References": references_content
}

# Quiz data: a list of dictionaries with question, options, and correct answer index
quizzes = [
    {
        "question": "1) What is C# primarily used for?",
        "options": [
            "Building .NET applications",
            "Low-level hardware programming",
            "Developing Linux kernel modules",
            "Solely for AI/ML algorithms"
        ],
        "answer": 0
    },
    {
        "question": "2) Which keyword introduces asynchronous programming in C#?",
        "options": [
            "async/await",
            "goto/await",
            "run/async",
            "waitfor"
        ],
        "answer": 0
    },
    {
        "question": "3) LINQ is used for:",
        "options": [
            "Networking operations",
            "Database schema migrations",
            "Querying data from in-memory collections",
            "Graphics rendering"
        ],
        "answer": 2
    },
    {
        "question": "4) What is the purpose of the 'using' statement in C#?",
        "options": [
            "To include namespaces",
            "To handle exceptions",
            "To ensure IDisposable objects are disposed",
            "To declare variables"
        ],
        "answer": 2
    },
    {
        "question": "5) Which design pattern ensures a class has only one instance?",
        "options": [
            "Factory Pattern",
            "Singleton Pattern",
            "Observer Pattern",
            "Decorator Pattern"
        ],
        "answer": 1
    }
]

# Progress file path
PROGRESS_FILE = "progress.json"

# ---------------------------
# Main Application Class
# ---------------------------

class CSharpTrainerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("C# Trainer - Professional Edition")
        self.geometry("1300x900")
        self.resizable(True, True)

        # State variables
        self.dark_mode = False
        self.current_module = None
        self.note_content = ""
        self.current_search_term = ""
        self.quiz_vars = []
        self.score = 0
        self.progress = self.load_progress()

        # Style configuration
        self.style = ttk.Style(self)
        self.set_light_mode()

        # Create menu
        self.create_menu()

        # Create main layout frames
        self.create_main_frames()

        # Navigation
        self.create_navigation()

        # Display default module
        self.display_content(modules["Introduction"])

    def create_menu(self):
        menubar = tk.Menu(self)

        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Toggle Dark Mode", command=self.toggle_dark_mode)

        notes_menu = tk.Menu(menubar, tearoff=0)
        notes_menu.add_command(label="View Notes", command=self.view_notes)
        notes_menu.add_command(label="Clear Notes", command=self.clear_notes)

        menubar.add_cascade(label="View", menu=view_menu)
        menubar.add_cascade(label="Notes", menu=notes_menu)

        self.config(menu=menubar)

    def create_main_frames(self):
        # Left Navigation Frame
        self.nav_frame = ttk.Frame(self, width=250, padding=10)
        self.nav_frame.pack(side='left', fill='y')

        # Top Frame (for search)
        self.top_frame = ttk.Frame(self, padding=10)
        self.top_frame.pack(side='top', fill='x')

        # Content Frame (main display area) with Scrollbar
        self.content_canvas = tk.Canvas(self, bg=self['bg'])
        self.content_canvas.pack(side='right', fill='both', expand=True)

        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.content_canvas.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.content_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Bind mousewheel to scroll
        self.content_canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Create a frame inside the canvas
        self.content_frame = ttk.Frame(self.content_canvas, padding=10)
        self.content_canvas.create_window((0, 0), window=self.content_frame, anchor='nw')

        # Configure resizing
        self.content_frame.bind("<Configure>", self.on_frame_configure)

        # Search Bar
        tk.Label(self.top_frame, text="Search:", font=('Segoe UI', 12)).pack(side='left')
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.top_frame, textvariable=self.search_var, width=50)
        self.search_entry.pack(side='left', padx=5)
        ttk.Button(self.top_frame, text="Search", command=self.search_content).pack(side='left')
        ttk.Button(self.top_frame, text="Clear Search", command=self.clear_search).pack(side='left', padx=(10,0))

    def on_frame_configure(self, event):
        self.content_canvas.configure(scrollregion=self.content_canvas.bbox("all"))

    def _on_mousewheel(self, event):
        # For Windows and MacOS
        if self.dark_mode:
            self.content_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            self.content_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def create_navigation(self):
        title_label = ttk.Label(self.nav_frame, text="C# Trainer", style='Title.TLabel', anchor='center')
        title_label.pack(pady=20)

        sep = ttk.Separator(self.nav_frame, orient='horizontal')
        sep.pack(fill='x', pady=10)

        for module_name in modules.keys():
            btn = ttk.Button(self.nav_frame, text=module_name, style='NavButton.TButton', 
                             command=lambda name=module_name: self.display_content(modules[name]))
            btn.pack(fill='x', pady=5)

        sep2 = ttk.Separator(self.nav_frame, orient='horizontal')
        sep2.pack(fill='x', pady=20)

        exit_btn = ttk.Button(self.nav_frame, text="Exit", command=self.quit, style='NavButton.TButton')
        exit_btn.pack(fill='x', pady=10)

    def display_content(self, content):
        self.current_module = content
        # Clear existing content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Insert title
        title = ttk.Label(self.content_frame, text=content["title"], style='Heading.TLabel', wraplength=900)
        title.pack(pady=(0,10))

        # Insert sections
        for section in content["sections"]:
            subheading = ttk.Label(self.content_frame, text=section["heading"], style='Subheading.TLabel', wraplength=900, justify='left')
            subheading.pack(anchor='w', pady=(10,5))

            content_text = section["content"]
            # Handle code blocks and regular text
            self.insert_content(section["content"])

        # Special handling for quizzes
        if content == quizzes_content:
            self.display_quiz()
        elif content == glossary_content:
            pass  # Additional handling if needed
        elif content == references_content:
            pass  # Additional handling if needed

        # Update progress if not quizzes
        if content != quizzes_content:
            self.mark_module_completed(content["title"])

    def insert_content(self, content):
        lines = content.split('\n')
        in_code_block = False
        code_text = ""

        for line in lines:
            if line.strip().startswith("```csharp"):
                in_code_block = True
                code_text = ""
                continue
            elif line.strip() == "```" and in_code_block:
                in_code_block = False

                # Create a frame for the code block and action button
                code_frame = ttk.Frame(self.content_frame)
                code_frame.pack(fill='x', pady=5)

                code_widget = scrolledtext.ScrolledText(code_frame, wrap=tk.WORD, font=("Consolas", 12), bg="#f5f5f5", height=10)
                code_widget.pack(side='left', fill='both', expand=True)
                code_widget.insert(tk.END, code_text)
                code_widget.configure(state='disabled')

                # Button to execute code
                exec_button = ttk.Button(code_frame, text="Execute Code", command=lambda c=code_text: self.execute_csharp_code(c))
                exec_button.pack(side='right', padx=10, pady=5)

                continue

            if in_code_block:
                code_text += line + '\n'
            else:
                if line.strip() == "":
                    ttk.Label(self.content_frame, text="", style='Content.TLabel').pack()
                else:
                    ttk.Label(self.content_frame, text=line, style='Content.TLabel', wraplength=900, justify='left').pack(anchor='w')

    def execute_csharp_code(self, code):
        # This method compiles and executes the given C# code snippet and shows the output.
        
        # Check if dotnet or csc is available
        compiler = None
        
        # Prefer dotnet if available
        if self.command_exists("dotnet"):
            compiler = "dotnet"
        elif self.command_exists("csc"):
            compiler = "csc"
        else:
            messagebox.showerror("Error", "No C# compiler found. Please install the .NET SDK or csc.")
            return

        with tempfile.TemporaryDirectory() as temp_dir:
            cs_file = os.path.join(temp_dir, "Program.cs")
            exe_file = os.path.join(temp_dir, "Program.dll") if compiler == "dotnet" else os.path.join(temp_dir, "Program.exe")

            # Write code to file
            with open(cs_file, "w", encoding="utf-8") as f:
                f.write(code)

            # Compile code
            if compiler == "dotnet":
                # Using dotnet CLI
                # Create a simple .csproj
                csproj_file = os.path.join(temp_dir, "Program.csproj")
                csproj_content = """<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net6.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>
"""
                with open(csproj_file, "w", encoding="utf-8") as f:
                    f.write(csproj_content)
                
                # Now run `dotnet build` and `dotnet run`
                build_result = subprocess.run(["dotnet", "build", csproj_file, "-c", "Release", "-o", temp_dir],
                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if build_result.returncode != 0:
                    messagebox.showerror("Compilation Error", build_result.stderr)
                    return

                run_result = subprocess.run(["dotnet", exe_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            else:
                # Using csc (Roslyn compiler)
                build_result = subprocess.run(["csc", "/out:" + exe_file, cs_file],
                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if build_result.returncode != 0:
                    messagebox.showerror("Compilation Error", build_result.stderr)
                    return

                # Run the compiled program
                run_result = subprocess.run([exe_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if run_result.returncode != 0:
                output = "Runtime Error:\n" + run_result.stderr
            else:
                output = run_result.stdout

            # Show output in a message box
            messagebox.showinfo("Program Output", output.strip())

    def command_exists(self, cmd):
        # Check if a command exists in PATH
        return any(
            os.access(os.path.join(path, cmd), os.X_OK)
            for path in os.environ["PATH"].split(os.pathsep)
        )

    def display_quiz(self):
        # Insert quiz UI at the end of the content_frame
        quiz_intro = ttk.Label(self.content_frame, text="Please answer the following questions:", style='Content.TLabel', wraplength=900, justify='left')
        quiz_intro.pack(pady=(10,10))

        self.quiz_vars = []
        for idx, quiz in enumerate(quizzes):
            q_label = ttk.Label(self.content_frame, text=quiz["question"], style='QuizQuestion.TLabel', wraplength=900, justify='left')
            q_label.pack(anchor='w', pady=(10,0))

            var = tk.IntVar(value=-1)
            self.quiz_vars.append((var, quiz["answer"]))
            for opt_idx, option in enumerate(quiz["options"]):
                rb = ttk.Radiobutton(self.content_frame, text=option, variable=var, value=opt_idx)
                rb.pack(anchor='w', padx=20)

        submit_btn = ttk.Button(self.content_frame, text="Submit", command=self.evaluate_quiz)
        submit_btn.pack(pady=20)

    def evaluate_quiz(self):
        score = 0
        for var, ans in self.quiz_vars:
            if var.get() == ans:
                score += 1
        messagebox.showinfo("Quiz Results", f"You scored {score} out of {len(self.quiz_vars)}")

        # Save progress
        self.mark_quiz_completed()

    def search_content(self):
        term = self.search_var.get().strip().lower()
        if not term:
            return

        # Clear previous highlights
        self.clear_highlights()

        for widget in self.content_frame.winfo_children():
            if isinstance(widget, ttk.Label):
                text = widget.cget("text").lower()
                if term in text:
                    widget.config(style='Highlight.TLabel')

    def clear_search(self):
        self.search_var.set("")
        self.clear_highlights()

    def clear_highlights(self):
        for widget in self.content_frame.winfo_children():
            if isinstance(widget, ttk.Label):
                # Reset to normal style
                if widget.cget("text").startswith("**") and widget.cget("text").endswith("**"):
                    widget.config(style='Subheading.TLabel')
                else:
                    widget.config(style='Content.TLabel')

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.set_dark_mode()
        else:
            self.set_light_mode()

    def set_light_mode(self):
        self.config(bg="#ffffff")
        self.style.theme_use('default')

        # Configure styles
        self.style.configure('Title.TLabel', font=('Segoe UI', 24, 'bold'), background="#ffffff", foreground="#000000")
        self.style.configure('Heading.TLabel', font=('Segoe UI', 20, 'bold'), background="#ffffff", foreground="#000000")
        self.style.configure('Subheading.TLabel', font=('Segoe UI', 16, 'bold'), background="#ffffff", foreground="#000000")
        self.style.configure('Content.TLabel', font=('Segoe UI', 12), background="#ffffff", foreground="#000000")
        self.style.configure('QuizQuestion.TLabel', font=('Segoe UI', 14, 'bold'), background="#ffffff", foreground="#000000")
        self.style.configure('Highlight.TLabel', font=('Segoe UI', 12), background="#ffff00", foreground="#000000")
        self.style.configure('NavButton.TButton', font=('Segoe UI', 12), background="#f0f0f0", foreground="#000000")
        self.style.configure('TButton', font=('Segoe UI', 12))
        self.style.configure('TLabel', background="#ffffff", foreground="#000000")

    def set_dark_mode(self):
        self.config(bg="#2e2e2e")
        self.style.theme_use('clam')

        # Configure styles
        self.style.configure('Title.TLabel', font=('Segoe UI', 24, 'bold'), background="#2e2e2e", foreground="#ffffff")
        self.style.configure('Heading.TLabel', font=('Segoe UI', 20, 'bold'), background="#2e2e2e", foreground="#ffffff")
        self.style.configure('Subheading.TLabel', font=('Segoe UI', 16, 'bold'), background="#2e2e2e", foreground="#ffffff")
        self.style.configure('Content.TLabel', font=('Segoe UI', 12), background="#2e2e2e", foreground="#ffffff")
        self.style.configure('QuizQuestion.TLabel', font=('Segoe UI', 14, 'bold'), background="#2e2e2e", foreground="#ffffff")
        self.style.configure('Highlight.TLabel', font=('Segoe UI', 12), background="#555555", foreground="#ffffff")
        self.style.configure('NavButton.TButton', font=('Segoe UI', 12), background="#444444", foreground="#ffffff")
        self.style.configure('TButton', font=('Segoe UI', 12), background="#444444", foreground="#ffffff")
        self.style.configure('TLabel', background="#2e2e2e", foreground="#ffffff")

    def view_notes(self):
        notes_win = tk.Toplevel(self)
        notes_win.title("My Notes")
        notes_win.geometry("700x500")
        notes_win.resizable(False, False)

        tk.Label(notes_win, text="Write your notes here:", font=("Segoe UI", 14, "bold")).pack(pady=10)
        text_area = scrolledtext.ScrolledText(notes_win, wrap=tk.WORD, font=("Segoe UI", 12))
        text_area.pack(fill='both', expand=True, padx=10, pady=10)
        text_area.insert(tk.END, self.note_content)

        def save_notes():
            self.note_content = text_area.get("1.0", tk.END).strip()
            self.save_progress()
            notes_win.destroy()

        ttk.Button(notes_win, text="Save Notes", command=save_notes).pack(pady=10)

    def clear_notes(self):
        self.note_content = ""
        messagebox.showinfo("Notes", "Your notes have been cleared.")

    def mark_module_completed(self, module_title):
        if module_title not in self.progress.get("completed_modules", []):
            self.progress.setdefault("completed_modules", []).append(module_title)
            self.save_progress()

    def mark_quiz_completed(self):
        if "Quizzes" not in self.progress.get("completed_quizzes", []):
            self.progress.setdefault("completed_quizzes", []).append("Quizzes")
            self.save_progress()

    def load_progress(self):
        if os.path.exists(PROGRESS_FILE):
            with open(PROGRESS_FILE, "r") as f:
                return json.load(f)
        else:
            return {}

    def save_progress(self):
        with open(PROGRESS_FILE, "w") as f:
            json.dump(self.progress, f, indent=4)

# ---------------------------
# Main Function
# ---------------------------

def main():
    app = CSharpTrainerApp()
    app.mainloop()

if __name__ == "__main__":
    main()
