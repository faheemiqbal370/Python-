class StudentSystem:
    def __init__(self):
        self.students = []  

    def add_student(self, sid, name, marks):
        self.students.append((sid, name, marks))

    def search_by_id(self, sid):
        for s in self.students:
            if s[0] == sid:
                return s
        return None

    def sort_by_marks(self):
        return sorted(self.students, key=lambda x: x[2], reverse=True)

    def count_fail(self):
        return sum(1 for s in self.students if s[2] < 35)

    def top_5(self):
        sorted_list = self.sort_by_marks()
        return sorted_list[:5]



sys = StudentSystem()
sys.add_student(1, "A", 80)
sys.add_student(2, "B", 30)
sys.add_student(3, "C", 95)
sys.add_student(4, "D", 40)

print("Search:", sys.search_by_id(3))
print("Sorted:", sys.sort_by_marks())
print("Fails:", sys.count_fail())
print("Top 5:", sys.top_5())
