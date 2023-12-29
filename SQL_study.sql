--选择全部
select 
  id,device_id,
  gender,
  age,
  university,province
from user_profile;
--选择多列
select
device_id,
gender,
age,
university
from user_profile
where device_id is not NULL
--删除重复
select
university
from user_profile
group by university
--排序
SELECT name, age, salary
FROM employees
ORDER BY age DESC, salary ASC; --先降序排，如果相同就按工资升序排
--选出前两个
select device_id
from user_profile
limit 2
--题目：现在你需要查看前2个用户明细设备ID数据，并将列名改为 'user_infos_example',，请你从用户信息表取出相应结果。
SELECT device_id AS user_infos_example
FROM user_profile
LIMIT 2;
--题目：现在运营想要筛选出所有北京大学的学生进行用户调研，请你从用户信息表中取出满足条件的数据，结果返回设备id和学校。
SELECT device_id, university from user_profile
where university = '北京大学'
--题目：现在运营想要针对24岁以上的用户开展分析，请你取出满足条件的设备ID、性别、年龄、学校。
select device_id, gender, age, university from user_profile
where age >24

select device_id, gender, age from user_profile
where age >=20 and age<=23
--题目：现在运营想要查看除复旦大学以外的所有用户明细，请你取出相应数据
SELECT device_id, gender, age, university from user_profile
where university is not '复旦大学'
--题目：现在运营想要找到学校为北大、复旦和山大的同学进行调研，请你取出相关数据。
SELECT device_id, gender, age, university, gpa from user_profile
where university in ('复旦大学','北京大学','山东大学') 
--题目：现在运营想查看所有大学中带有北京的用户的信息，请你取出相应数据。
SELECT device_id, age, university from user_profile
where university like '%北京%'
--题目：运营想要知道复旦大学学生gpa最高值是多少，请你取出相应数据
select max(gpa) from user_profile
where university='复旦大学'
--题目：现在运营想要看一下男性用户有多少人以及他们的平均gpa是多少，用以辅助设计相关活动，请你取出相应数据。
select 
count(case when gender='male' then 1 end) as male_nums,
avg(case when gender='male' then gpa end) as avg_gpa
from user_profile

--题目：现在运营想要对每个学校不同性别的用户活跃情况和发帖数量进行分析，请分别计算出每个学校每种性别的用户数、30天内平均活跃天数和平均发帖数量。
select 
gender, 
university,
COUNT(device_id) as user_num,
AVG(active_days_within_30) as avg_active_day,
AVG(question_cnt) as avg_question_cnt
from user_profile
group by gender, university
--题目：现在运营想要查看所有来自浙江大学的用户题目回答明细情况，请你取出相应数据
--内连接查询
select question_practice_detail.device_id,question_id,result 
from question_practice_detail 
INNER JOIN user_profile on question_practice_detail.device_id = user_profile.device_id and user_profile.university="浙江大学";
--运营想要了解每个学校答过题的用户平均答题数量情况，请你取出数据。
select university, 
count(question_practice_detail.question_id)/count(distinct question_practice_detail.device_id) as avg_answer_cnt
from user_profile inner join question_practice_detail on user_profile.device_id= question_practice_detail.device_id
GROUP by university
--题目：运营想要计算一些参加了答题的不同学校、不同难度的用户平均答题量，请你写SQL取出相应数据
select 
university,
question_detail.difficult_level,
count(question_practice_detail.question_id)/count(distinct question_practice_detail.device_id) as avg_answer_cnt
from user_profile 
inner join question_practice_detail on user_profile.device_id=question_practice_detail.device_id
inner join question_detail on question_practice_detail.question_id=question_detail.question_id
group by university, question_detail.difficult_level
--题目：现在运营想要将用户划分为25岁以下和25岁及以上两个年龄段，分别查看这两个年龄段用户数量，改变分组名称
SELECT
    CASE
        WHEN age IS NULL OR age < 25 THEN '25岁以下'
        ELSE '25岁及以上'
    END AS age_cut,
    COUNT(*) AS number
FROM
    user_profile
GROUP BY
    CASE
        WHEN age IS NULL OR age < 25 THEN '25岁以下'
        ELSE '25岁及以上'
    END;
--题目：现在运营想要计算出2021年8月每天用户练习题目的数量，请取出相应数据。
SELECT DAY(date) AS day, COUNT(*) AS question_cnt
FROM question_practice_detail
WHERE YEAR(date) = 2021 AND MONTH(date) = 8
GROUP BY DAY(date);
--分割字符串
SELECT 
    SUBSTRING_INDEX(profile, ',', -1) AS gender,
    COUNT(*) AS number
FROM user_submit
GROUP BY gender;
--最低gpa
select device_id,university,gpa
from user_profile
where (university, gpa) in (select university,min(gpa) from user_profile group by university)
order by university
--
-- Write only the SQL statement that solves the problem and nothing else
select
name,
age
from people
where age in (select min(age) from people)