# Finger Print Tag Group

---

TODO LIST

+ Scraping from various website and store the information in the json format.
+ Try with different NLP keyword extraction technique for tagging generation
+ Figure out how to create a database from https://musicbrainz.org/doc/MusicBrainz_Database/Download and cross-reference songs with hypem.com to check song reviews and create tags by using some sort of NLP api to check them for tags or scrape them with a preset group of tags
+ Link related tags together (possibly with some sort of NLP)

---

JSON FILE SPECIFICATION

```
{
	"name" : "...",
	"artist" : "...", //unknonwn
	"genre" : " "...",
	"album" : "...",
	"gender" : "...",
	"release_date" : "MM/DD/YYYY" // ? to substitute,
	"instrument" : ["...",...],
	"run_time" : "mm:ss", // 00:00
	"article" : "...",
	"keywords" : ["...", ...]
}
```
