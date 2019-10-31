create view TNS as select Movie.mID, Reviewer.rID, Movie.title, Reviewer.name, Rating.stars, Rating.ratingDate from Movie, Reviewer, Rating where Rating.rID=Reviewer.rID and Rating.mID=Movie.mID;

select max(year) from Movie where Movie.title in (select title from TNS where name="Chris Jackson");

create view RatingStats as select TNS.title, count(*) as 'No_reviews', avg(stars) as 'Average_stars' from TNS group by title;

select title from RatingStats where Average_stars=(select max(Average_stars) from RatingStats where No_reviews>2);

select Movie.mID, re.rID, Rating.stars from Movie, Reviewer re, Rating where Rating.rID=Reviewer.rID and Rating.mID=Movie.mID and Rating.stars=(select max(stars) from Rating where rID=re.rID);

select R.name,R1.name,M.title from Reviewer R,Reviewer R1,Movie M where (R.rID,R1.rID,M.mID) in (select distinct r1.rID,r2.rID,r1.mID from Favourites r1,Favourites r2 where r1.mID=r2.mID and r1.rID<>r2.rID and r1.rID<r2.rID);
