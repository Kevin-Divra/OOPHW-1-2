from user.user import User
from Dosen import Dosen
from SuperAdmin import SuperAdmin
from Mahasiswa import Mahasiswa


class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.user_id = user_id
        self.password = password
        self.add_schedule = []

    def login(self, id, password):
        if id == self.user_id and password == self.password:
            return True
        else:
            return False

    def create_user_account(self, user_type, *args):

        if user_type == "Mahasiswa":
            return Mahasiswa(*args)
        elif user_type == "Dosen":
            return Dosen(*args)
        elif user_type == "SuperAdmin":
            return SuperAdmin(*args)
        
    def add_schedule_to_course(self, course, schedule):
        course.add_schedule(schedule)
        print(f"Jadwal berhasil ditambahkan ke kursus {course.name}.")
    
    def student_payment(self, mahasiswa, tagihan):
        if isinstance(mahasiswa, Mahasiswa):
             print(f"Tagihan sebesar {tagihan} berhasil diinputkan untuk {mahasiswa.get_name()}.")
        else:
            print("Gagal menginputkan tagihan. Objek yang diberikan bukan merupakan instance dari kelas Mahasiswa.")
  