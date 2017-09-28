select aaa.division_name, aaa.xxx from (
select division_name, count(*) as xxx, d.division_id
from division d inner join member m on d.division_id = m.division_id
group by division_name, d.division_id
) as aaa
order by aaa.division_id