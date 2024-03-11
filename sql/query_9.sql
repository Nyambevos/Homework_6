SELECT sub.subject_name 
FROM grades as e
LEFT JOIN students as s ON e.student_id = s	.id
LEFT JOIN subjects as sub on e.subject_id =	sub.id 
--WHERE s.name = 'Christopher Wang'
WHERE s.id = 2
;