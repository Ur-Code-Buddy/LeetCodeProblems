class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        rotation = 0
        
        while sandwiches:
            
            std = students.pop(0)
            
            if std == sandwiches[0]:
                sandwiches.pop(0)
                rotation = 0
            else:
                students.append(std)
                rotation += 1
            if rotation >= len(students):
                return len(students)
                
            