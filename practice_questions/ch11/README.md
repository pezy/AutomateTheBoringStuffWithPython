# Chapter 11 – Web Scraping

> Q: 1. Briefly describe the differences between the webbrowser, requests, BeautifulSoup, and selenium modules.

`webbrowser` can launch a web browser to a specific URL by `open()`;
`requests` can download files and pages from the Web.
`beautifulSoup` module parses HTML.
`selenium` launch and control a browser.

> Q: 2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?

Response object. `getText()`.

> Q: 3. What Requests method checks that the download worked?

`raise_for_status()`

> Q: 4. How can you get the HTTP status code of a Requests response?

`status_code`

> Q: 5. How do you save a Requests response to a file?

```py
saveFile = open('SaveFile', 'wb')
for chunk in res.iter_content(100000):
    saveFile.write(chunk)
saveFile.close()
```

> Q: 6. What is the keyboard shortcut for opening a browser’s developer tools?

F12

> Q: 7. How can you view (in the developer tools) the HTML of a specific element on a web page?

Inspect Element

> Q: 8. What is the CSS selector string that would find the element with an id attribute of main?

`#main`

> Q: 9. What is the CSS selector string that would find the elements with a CSS class of highlight?

`.highlight`

> Q: 10. What is the CSS selector string that would find all the `<div>` elements inside another `<div>` element?

`div div`

> Q: 11. What is the CSS selector string that would find the `<button>` element with a value attribute set to favorite?

`button[value='favorite']`

> Q: 12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element `<div>`Hello world!`</div>`. How could you get a string 'Hello world!' from the Tag object?

spam.getText()

> Q: 13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?

linkElem.attrs

> Q: 14. Running import selenium doesn’t work. How do you properly import the selenium module?

`from selenium import webdriver`

> Q: 15. What’s the difference between the find_element_* and find_elements_* methods?

one vs a list.

> Q: 16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?

`click()` and `send_keys()`

> Q: 17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with Selenium?

`submit()`

> Q: 18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with Selenium?

`forward()`, `back()`, `refresh()`
