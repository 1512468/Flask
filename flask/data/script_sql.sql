CREATE TABLE "news" (
	"id"	INTEGER,
	"subject"	TEXT NOT NULL,
	"description"	TEXT,
	"image"	TEXT NOT NULL,
	"original_url"	TEXT,
	"category_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);

