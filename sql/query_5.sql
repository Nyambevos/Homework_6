SELECT s.subject_name, t.name 
FROM subjects as s
LEFT JOIN teachers as t ON s.teacher_id = t.id
--WHERE t.name = 'Gabriel Miller'
WHERE t.id = 3;