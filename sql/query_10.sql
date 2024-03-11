SELECT sub.subject_name 
FROM grades as e
LEFT JOIN students as s ON e.student_id = s	.id
LEFT JOIN subjects as sub on e.subject_id =	sub.id
LEFT JOIN teachers as t ON sub.teacher_id  = t.id 
--WHERE s.name = 'Christopher Wang' and t.name = 'Robin Sanchez'
WHERE s.id = 2 and t.id = 5
;