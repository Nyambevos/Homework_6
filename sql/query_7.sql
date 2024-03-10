SELECT s.name, e.grade, sg.students_group, sub.subject_name 
FROM grades as e
LEFT JOIN subjects as sub ON e.subject_id = sub.id
LEFT JOIN students as s ON e.student_id = s.id
LEFT JOIN students_groups as sg ON s.group_id  = sg.id
--WHERE sub.subject_name = 'Engineer, automotive'
WHERE sub.id = 2 AND sg.students_group = 2;