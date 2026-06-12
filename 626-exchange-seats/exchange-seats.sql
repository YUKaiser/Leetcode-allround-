# Write your MySQL query statement below
select id,Case
            when id%2=0 then LAG(student,1) Over(Order by id)
            when id%2!=0 then ifNULL(Lead(student,1) Over(Order by id),student)

            End
            as student
        from Seat