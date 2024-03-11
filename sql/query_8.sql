SELECT t.name, ROUND(AVG(e.grade), 2) AS average_grade
FROM grades as e
LEFT JOIN teachers as t ON e.student_id = t.id
--WHERE t.name = 'William Le'
WHERE t.id = 2
;