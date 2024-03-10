SELECT s.name, sub.subject_name, ROUND(AVG(e.grade), 2) AS average_grade
FROM grades as e
LEFT JOIN subjects as sub ON e.subject_id = sub.id
LEFT JOIN students as s ON e.student_id = s.id
WHERE sub.id = 3
GROUP BY s.name
ORDER BY average_grade DESC LIMIT 1;