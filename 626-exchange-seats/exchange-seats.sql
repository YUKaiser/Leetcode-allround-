select Case 
          when id=(select max(id) from Seat) and id%2!=0 then id
          When id%2!=0 then id+1
          
          else id-1
          end as id,student
          from seat
          order by id