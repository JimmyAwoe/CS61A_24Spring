CREATE TABLE parents AS
  SELECT 'abraham' AS parent, 'barack' AS child UNION
  SELECT 'abraham'          , 'clinton'         UNION
  SELECT 'delano'           , 'herbert'         UNION
  SELECT 'fillmore'         , 'abraham'         UNION
  SELECT 'fillmore'         , 'delano'          UNION
  SELECT 'fillmore'         , 'grover'          UNION
  SELECT 'eisenhower'       , 'fillmore';

CREATE TABLE dogs AS
  SELECT 'abraham' AS name, 'long' AS fur, 26 AS height UNION
  SELECT 'barack'         , 'short'      , 52           UNION
  SELECT 'clinton'        , 'long'       , 47           UNION
  SELECT 'delano'         , 'long'       , 46           UNION
  SELECT 'eisenhower'     , 'short'      , 35           UNION
  SELECT 'fillmore'       , 'curly'      , 32           UNION
  SELECT 'grover'         , 'short'      , 28           UNION
  SELECT 'herbert'        , 'curly'      , 31;

CREATE TABLE sizes AS
  SELECT 'toy' AS size, 24 AS min, 28 AS max UNION
  SELECT 'mini'       , 28       , 35        UNION
  SELECT 'medium'     , 35       , 45        UNION
  SELECT 'standard'   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child 
  FROM parents as a, dogs as b 
  WHERE b.name=a.parent 
  ORDER BY -b.height;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT  dogs.name, sizes.size
  FROM dogs, sizes
  WHERE dogs.height <= sizes.max and dogs.height > sizes.min;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.name AS oldname, b.name AS yonname, a.size AS size
  FROM size_of_dogs AS a, size_of_dogs AS b
  WHERE a.size = b.size and a.name < b.name and a.size <> 'mini'
  GROUP BY a.size;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT 'The two siblings, ' || oldname || ' and ' || yonname || ', have the same size: ' || size
  FROM siblings;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT dogs.fur, max(dogs.height) - min(dogs.height)
  FROM dogs
  GROUP BY dogs.fur 
  HAVING min(dogs.height) > (avg(dogs.height) * 0.7) and max(dogs.height) <= (avg(dogs.height) * 1.3);


