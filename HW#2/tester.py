from Admin import Admin
from courses import Course


def main():
    admin = Admin("A1", "Kevin", "Kevin@si.ukrida.ac.id", "adminpass")

    id = input("Masukkan id: ")
    password = input("Masukkan Password: ")

    if admin.login(id, password):
        print("Login Berhasil")

        print('\n')

        mahasiswa = admin.create_user_account("Mahasiswa", "M1", "kevin", "kecin@gmail.com", "studentpass", "E123")
        dosen = admin.create_user_account("Dosen", "D1", "ABDUL", "ABDUL@gmail.com", "dosenpass", "E321")

        dsp_course = Course("siwp1001", "Algorithma", "Introduction to programming and algorithms fundamental")
        pbo_course = Course("siwp2005", "PBO", "Object oriented programming")

        admin.add_schedule_to_course(dsp_course, "Senin, 08:00 - 10:00")
        admin.add_schedule_to_course(pbo_course, "Selasa, 10:00 - 12:00")

        if mahasiswa:
            mahasiswa.enroll_in_course(dsp_course)
        if dosen:
            dosen.teach_course(pbo_course)

        for user in [mahasiswa, dosen]:
            if mahasiswa:
                mahasiswa.view_schedule(dsp_course)
        else:
            dosen.view_schedule(pbo_course)

        for user in [dosen]:
            if user:
                user.upload_grades(dsp_course, mahasiswa.get_user_id(), 85)

        print(dsp_course.view_grades(mahasiswa.get_user_id()))

        for user in [mahasiswa]:
            if user:
                print(f"user {user.get_user_id()} can log in: {user.login(user._email, 'studentpass')}")
        
        for user in [dosen]:
            if user:
                print(f"user {user.get_user_id()} can log in: {user.login(user._email, 'dosenpass')}")
        
        for user in [admin]:
            if user:
                print(f"user {user.get_user_id()} can log in: {user.login(user._email, 'SuperAdmin')}")
        
        for user in [admin]:
            if user:
                admin.student_payment(mahasiswa, 500000)
            
    else:
        print("Login gagal")


if __name__ == "__main__":
    main()
