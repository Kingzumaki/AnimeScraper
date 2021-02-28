# AnimeScraper
This is a webscraper that scrapes anime details such as a summary and the anime's genres using the BS4 module as well as the requests module

<h1> Anime Scraper </h1>
Anime scraper uses python's requests and BeautifulSoup module to scrape anime titles. The data is fetched from 4Anime. 

<h2> The Innerworking </h2>

The script first fetches URL output which depends on the user's anime input. The requests.get() and variable.content helps in fetching the page source and the page content. A soup object is created from the page content using BeautifulSoup.<br/>The soup objects is then filtered multiple time to obtain the desired results.

<h2> Libraries Required </h2>
<ol>
  <li> BeautifulSoup </li>
  <li> requests </li>
</ol>
