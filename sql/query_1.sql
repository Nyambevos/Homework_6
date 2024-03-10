SELECT s.name, ROUND(AVG(e.grade), 2) AS average_grade
FROM grades as e
LEFT JOIN students as s ON e.student_id = s.id
GROUP BY s.name
ORDER BY average_grade DESC
LIMIT 5;