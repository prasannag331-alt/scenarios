class Course:
    """Base class representing a general course."""
    def _init_(self, course_name: str, duration: str, fee: float):
        self.course_name = course_name
        self.duration = duration
        self.fee = fee
        self.category = "General"

    def display_info(self):
        """Prints the details of the course."""
        print(f"| {self.course_name:<25} | {self.category:<12} | {self.duration:<12} | ${self.fee:<8.2f} |")


# Categorize courses using inheritance
class ShortTermCourse(Course):
    """Subclass for Short-Term courses (e.g., days or weeks)."""
    def _init_(self, course_name: str, duration: str, fee: float):
        super()._init_(course_name, duration, fee)
        self.category = "Short-Term"


class LongTermCourse(Course):
    """Subclass for Long-Term courses (e.g., months or years)."""
    def _init_(self, course_name: str, duration: str, fee: float):
        super()._init_(course_name, duration, fee)
        self.category = "Long-Term"


class Institute:
    """Class to manage and display all courses within the institute."""
    def _init_(self, institute_name: str):
        self.institute_name = institute_name
        self.courses = []

    def add_course(self, course: Course):
        """Adds a course object to the institute repository."""
        self.courses.append(course)

    def display_all_courses(self):
        """Displays all courses in a structured table format."""
        print(f"\n=== Course Catalog for {self.institute_name} ===")
        if not self.courses:
            print("No courses available at the moment.")
            return
        
        # Table Header
        print("-" * 67)
        print(f"| {'Course Name':<25} | {'Category':<12} | {'Duration':<12} | {'Fee':<9} |")
        print("-" * 67)
        
        # Table Body
        for course in self.courses:
            course.display_info()
            
        print("-" * 67)


# --- Demonstration of the System ---
if _name_ == "_main_":
    # 1. Create an Institute instance
    my_institute = Institute("Tech Academy")

    # 2. Create categorized course objects
    course1 = ShortTermCourse("Python Crash Course", "2 Weeks", 150.00)
    course2 = ShortTermCourse("Data Visualization Intro", "5 Days", 99.00)
    course3 = LongTermCourse("Full-Stack Software Eng.", "6 Months", 2500.00)
    course4 = LongTermCourse("Data Science Bootcamp", "9 Months", 3200.00)

    # 3. Add courses to the institute
    my_institute.add_course(course1)
    my_institute.add_course(course2)
    my_institute.add_course(course3)
    my_institute.add_course(course4)

    # 4. Display all courses
    my_institute.display_all_courses()
