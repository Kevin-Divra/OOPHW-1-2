from user.user import User

class Mahasiswa(User):
    def __init__(self, user_id, name, email, password, enrollment_id):
        super().__init__(user_id, name, email, password)
        self.enrollment_id = enrollment_id
        self.courses = []
        self.grades = []
        self.schedules = []

    def enroll_in_course(self, course):
        self.courses.append(course)
        course.add_student(self)
    
    def view_schedule(self, course_id):
        if course_id in self.schedules:
            return self.schedules[course_id]
        else:
            return "Jadwal tidak tersedia"

    def lihat_jadwal(self):
        if not self.courses:
            print("Anda belum terdaftar pada kursus manapun.")
        else:
            print("Jadwal mata kuliah:")
            for course in self.courses:
                print(f"{course.name}: {course.schedule}")

    def get_name(self):
        return self._name
