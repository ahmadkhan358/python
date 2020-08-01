from faker import Faker
import random
import csv
import os

class gererate_fake_salaries():
    def generate(self, r):
        fake = Faker()
        row_list = [["Position level", "Salary"]]
        for i in range(r):
            salary = round(random.randint(90000,1220000)/1000)*1000
            job = fake.job()
            job = job.split(',')[0]
            entry = [job, salary]
            row_list.append(entry)
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        with open(desktop+"/Position_Salaries.csv", "w", newline='') as myFile:
            writer = csv.writer(myFile)
            writer.writerows(row_list)
            myFile.close()


if __name__ == "__main__":
    salary_data = gererate_fake_salaries()
    salary_data.generate(1000)