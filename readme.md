## Pastebin Infosec Threat Hunter
A simple python program monitors patebin for DataLeaks.

Approach:
-  scrape pastebin archive page ✅
-  find all hrefs => which inturn gets us post id's ✅
-  make a forloop and traverse through all the hrefs ✅
-  skip the first 3 a tags coz they are basically nav links and skipped when i see an empty href because after that its just footer links.. ✅
-  now we need to scrape individual posts or and get the data 
 
