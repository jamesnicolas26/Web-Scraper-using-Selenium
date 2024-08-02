from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scrape_with_selenium(url):
    """Scrape data from a webpage using Selenium."""

    # Set up the web driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Open the webpage
        driver.get(url)

        # Find elements (e.g., titles of articles)
        titles = driver.find_elements(By.TAG_NAME, 'h2')
        for title in titles:
            print(title.text)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()


def main():
    url = "https://www.w3schools.com/python/python_mongodb_insert.asp"  # Replace with the desired URL
    scrape_with_selenium(url)


if __name__ == "__main__":
    main()
