SELECT s.id, s.name 
FROM students as s
LEFT JOIN students_groups as sg ON s.group_id = sg.id
WHERE sg.students_group = 2