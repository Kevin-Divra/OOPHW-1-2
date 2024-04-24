class Course:
    def __init__(self, course_id, name, schedule):
        self.course_id = course_id
        self.name = name
        self.schedule = schedule
        self.students_enrolled = []  # List of Student objects
        self.students_schedule = []
        self.grades = {}  # Change to dictionary
        self.dosen_schedule = []
        self.course_materials = []
        
    def add_student(self, student):
        self.students_enrolled.append(student)

    def add_schedule(self, student):
        self.students_schedule.append(student)

    def add_instructor_schedule(self, dosen):
        self.dosen_schedule.append(dosen)
    
    def upload_grades(self, mahasiswa_id, grade):
        if mahasiswa_id in self.grades:
            print("Nilai untuk mahasiswa ini sudah diunggah sebelumnya.")
        else:
            self.grades[mahasiswa_id] = grade
            print("Nilai berhasil diunggah.")

    def view_grades(self, mahasiswa_id):
        if mahasiswa_id in self.grades:
            print("Grades: ")
            return self.grades[mahasiswa_id]
        else: 
            return "Nilai Mahasiswa ini Belum di Unggah"
    
    def lihat_tagihan(self):
        print(f"Total tagihan Anda adalah: {self.tagihan}")
    
    
