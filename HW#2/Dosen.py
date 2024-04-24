from user.user import User

class Dosen(User):
    def __init__(self, user_id, name, email, password, faculty_id):
        super().__init__(user_id, name, email, password)
        self.faculty_id = faculty_id
        self.courses_taught = []
        self.nilai = []     

    def teach_course(self, course):
        self.courses_taught.append(course)
    
    def upload_grades(self, course, mahasiswa_id, grade):
        course.upload_grades(mahasiswa_id, grade)

    def view_schedule(self, course):
        if course in self.courses_taught:
            print(f"Jadwal mengajar mata kuliah {course.name}: {course.schedule}")
        else:
            print("Anda belum mengajar mata kuliah ini.")        