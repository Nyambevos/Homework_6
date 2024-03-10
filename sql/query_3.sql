SELECT sub.subject_name, sg.students_group , ROUND(AVG(e.grade), 2) AS average_grade
FROM grades as e
LEFT JOIN subjects as sub ON e.subject_id = sub.id
LEFT JOIN students as s ON e.student_id = s.id
LEFT JOIN students_groups as sg ON s.group_id  = sg.id
--WHERE sub.subject_name = 'Engineer, automotive'
WHERE sub.id = 2
GROUP BY sg.students_group;