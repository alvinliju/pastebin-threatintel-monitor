## Pastebin Infosec Threat Hunter
A simple python program monitors patebin for DataLeaks.

Approach:
-  scrape pastebin archive page ✅
-  find all hrefs => which inturn gets us post id's ✅
-  make a forloop and traverse through all the hrefs ✅
-  skip the first 3 a tags coz they are basically nav links and skipped when i see an empty href because after that its just footer links.. ✅
-  we have atag which contains href attribute with postID's 
-  we can use patbin.com/raw/{id} -> url to get the raw data 
-  take the data and put it thorugh regex -> url to get the raw data
- build a regex.json or smthing and which will check if the posts has any leaks if yes log it if not do nothing 

