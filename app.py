from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(downloads_path="./downloads", headless=False)
    page = browser.new_page(accept_downloads=True)
    page.goto("https://unsplash.com/photos/tn57JI3CewI")

    with page.expect_download() as download_info:
        # Perform the action that initiates download
        page.click("._2vsJm")
    download = download_info.value
    # Wait for the download process to complete
    path = download.path()
    print(download.url, path)
    download.save_as("./downloads/img.jpg") 

    page.close()
    browser.close()
