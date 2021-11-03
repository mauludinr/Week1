SELECT
    *
FROM
    employees e
INNER JOIN jobs j ON e.job_id = j.job_id
INNER JOIN departments d ON e.department_id = d.department_id
INNER JOIN locations l ON d.location_id = l.location_id
INNER JOIN countries c ON l.country_id = c.country_id
INNER JOIN regions r ON c.region_id = r.region_id

WHERE
    e.salary < j.min_salary;