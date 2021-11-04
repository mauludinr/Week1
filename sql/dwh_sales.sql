create table dwh_sales as

select 
f.ArtistId,f.Name as ArtistName,e.AlbumId,e.Title as AlbumTitle, d.UnitPrice, 
SUM(Quantity) as Jumlah, (SUM(Quantity)*d.UnitPrice) as Total
from 
	Invoice b
	INNER join InvoiceLine a on a.InvoiceId = b.InvoiceId
	INNER join Track d on a.TrackId = d.TrackId
	INNER join Album e on d.AlbumId = e.AlbumId
	INNER join Artist f on e.ArtistId = f.ArtistId
GROUP BY e.AlbumId,f.ArtistId,d.UnitPrice

ORDER BY Jumlah DESC limit 50;
